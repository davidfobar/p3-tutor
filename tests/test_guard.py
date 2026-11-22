"""Tests of the tutor's keys guard, tutor/.claude/hooks/keys_guard.py.

Each test writes a hook input to the script's stdin and checks the exit code: 2 blocks, 0 allows.
The script runs from a copy in a throwaway workspace, so no test touches tutor/. None calls Claude.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TUTOR = Path(__file__).resolve().parent.parent / "tutor"
SCRIPT = Path(".claude", "hooks", "keys_guard.py")
BLOCK, ALLOW = 2, 0
CHECK = "python3 .claude/tools/lesson_check.py"


class GuardCase(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.base = Path(tmp.name).resolve()
        # a space in the path, and a folder named keys above the workspace
        self.ws = self.base / "keys" / "work space"
        (self.ws / SCRIPT).parent.mkdir(parents=True)
        shutil.copy(TUTOR / SCRIPT, self.ws / SCRIPT)
        for folder in ("keys", "quizzes", "lessons", "drafts"):
            (self.ws / folder).mkdir()
        (self.ws / "keys" / "0001.json").write_text('{"answer": "SECRET"}')
        (self.ws / "quizzes" / "0001.json").write_text("{}")
        (self.ws / "MISSION.md").write_text("mission")

    def run_guard(self, stdin):
        return subprocess.run([sys.executable, "-I", str(self.ws / SCRIPT)], input=stdin,
                              capture_output=True, text=True, timeout=20)

    def call(self, tool, args, agent=None, agent_id="a1", cwd=None):
        data = {"hook_event_name": "PreToolUse", "tool_name": tool, "tool_input": args, "cwd": str(cwd or self.ws)}
        if agent:
            data["agent_type"] = agent
            if agent_id:
                data["agent_id"] = agent_id
        return self.run_guard(json.dumps(data))

    def expect(self, code, tool, key, values, **who):
        for value in values:
            with self.subTest(tool=tool, value=value, **who):
                result = self.call(tool, {key: value}, **who)
                self.assertEqual(result.returncode, code, result.stderr)
                self.assertNotIn("SECRET", result.stdout + result.stderr)
                if code == BLOCK:
                    self.assertIn("keys guard: blocked", result.stderr)


class MainConversationTests(GuardCase):
    def test_read_of_a_key_is_blocked_however_it_is_spelled(self):
        self.expect(BLOCK, "Read", "file_path", [
            "keys/0001.json", "./keys/0001.json", str(self.ws / "keys" / "0001.json"), "lessons/../keys/0001.json",
            "keys\\0001.json", "KEYS/0001.json", " keys/0001.json ", "keys./0001.json", "keys//0001.json", "keys",
            "../../elsewhere/keys/0001.json",
        ])

    def test_read_relative_to_another_working_folder_is_blocked(self):
        self.expect(BLOCK, "Read", "file_path", ["0001.json"], cwd=self.ws / "keys")
        self.expect(BLOCK, "Read", "file_path", ["../keys/0001.json"], cwd=self.ws / "lessons")

    @unittest.skipIf(os.name == "nt", "symlinks need privileges on Windows")
    def test_read_through_a_link_is_blocked(self):
        (self.ws / "folder-link").symlink_to(self.ws / "keys")
        (self.ws / "file-link").symlink_to(self.ws / "keys" / "0001.json")
        self.expect(BLOCK, "Read", "file_path", ["folder-link/0001.json", "file-link"])

    def test_other_reads_work(self):
        self.expect(ALLOW, "Read", "file_path", [
            "MISSION.md", "quizzes/0001.json", str(self.ws / "quizzes" / "0001.json"), "drafts/0002-key-v1.json",
            "lessons/api-keys.html", "monkeys/notes.md",
        ])

    def test_grep_in_keys_or_over_them_is_blocked(self):
        self.expect(BLOCK, "Grep", "path", [
            "keys", "keys/0001.json", ".", "", "./", str(self.ws), "..", "/", "lessons/..", str(self.base),
        ])
        self.assertEqual(self.call("Grep", {"pattern": "answer"}).returncode, BLOCK)
        self.assertEqual(self.call("Grep", {"pattern": "x", "path": "lessons", "glob": "keys/*"}).returncode, BLOCK)

    def test_grep_in_a_named_place_works(self):
        self.expect(ALLOW, "Grep", "path", ["lessons", "quizzes/0001.json", "MISSION.md", str(self.ws / "drafts")])

    def test_glob_that_names_keys_is_blocked(self):
        self.expect(BLOCK, "Glob", "pattern", [
            "keys/*", "**/keys/**", "k*ys/*", "[k]eys/*", "{lessons,keys}/*", str(self.ws / "keys" / "*"),
        ])
        self.assertEqual(self.call("Glob", {"pattern": "*", "path": "keys"}).returncode, BLOCK)

    def test_glob_that_lists_names_works(self):
        self.expect(ALLOW, "Glob", "pattern", [
            "**/*", "*", "**/*.md", "lessons/*", "{quizzes,drafts}/**", str(self.ws / "lessons" / "*"),
        ])

    def test_bash_that_could_reach_a_key_is_blocked(self):
        self.expect(BLOCK, "Bash", "command", [
            "cat keys/0001.json", "cat k*/0001.json", "cat ke''ys/0001.json", 'cat "$D/0001.json"',
            "D=keys; cat $D/0001.json", "grep -r answer .", "cd keys && cat 0001.json", "cat < keys/0001.json",
            "echo $(cat keys/0001.json)", "echo `cat keys/0001.json`", "echo ok; cat keys/0001.json",
            "echo ok\ncat keys/0001.json", "echo ok & cat keys/0001.json", "echo ok;cat keys/0001.json",
            "ls keys", "ls ke''ys", "find keys", "find . -name keys", "find . -exec cat {} +",
            "find -files0-from keys/0001.json", "date -f keys/0001.json", "git show HEAD:tutor/keys/0001.json",
            "python3 -c 'print(open(\"ke\"+\"ys/0001.json\").read())'", "env cat keys/0001.json", "bash -c ls",
            f"{CHECK} keys/0001.json", f"{CHECK} k*/0001.json", "python3 drafts/lesson_check.py drafts/a.html",
            "echo 'unclosed", "ls 2>/dev/null; cat keys/0001.json",
        ])

    def test_harmless_bash_works(self):
        self.expect(ALLOW, "Bash", "command", [
            "ls lessons", "ls -la", "ls lessons 2>/dev/null", "pwd", "date +%F", "sleep 1; echo waiting",
            "find lessons -type f", "find . -name '*.html'", f"{CHECK} drafts/0001-x.html",
            f'{CHECK} "drafts/0001-x.html" 2>&1',
        ])

    def test_monitor_follows_the_shell_rules(self):
        self.expect(BLOCK, "Monitor", "command", ["cat keys/0001.json"])
        self.expect(ALLOW, "Monitor", "command", ["sleep 1"])

    def test_a_skill_cannot_be_handed_a_mention_of_a_key(self):
        # Claude Code pastes an @-mentioned file into the conversation without a Read call
        self.expect(BLOCK, "Skill", "args", [
            "see @keys/0001.json", "@./keys/0001.json", '@"keys/0001.json"', "@KEYS/0001.json", "@lessons/../keys/0001.json",
        ])
        self.expect(ALLOW, "Skill", "args", ["grade s1", "explain @dataclass", "what are API keys?", ""])

    def test_memory_files_cannot_be_written(self):
        # an @keys/0001.json line in a CLAUDE.md loads the key when the next session starts
        for tool in ("Write", "Edit"):
            self.expect(BLOCK, tool, "file_path", ["CLAUDE.md", "CLAUDE.local.md", "lessons/claude.md"])
        self.expect(ALLOW, "Read", "file_path", ["CLAUDE.md"])

    def test_powershell_is_blocked(self):
        self.expect(BLOCK, "PowerShell", "command", ["Get-Content keys/0001.json", "gc k*\\0001.json"])

    def test_edit_of_a_key_is_blocked(self):
        for tool in ("Edit", "MultiEdit"):
            self.expect(BLOCK, tool, "file_path", ["keys/0001.json"])
        self.expect(BLOCK, "NotebookEdit", "notebook_path", ["keys/0001.ipynb"])
        self.expect(ALLOW, "Edit", "file_path", ["NOTES.md"])

    def test_a_new_key_may_be_written_once(self):
        self.expect(ALLOW, "Write", "file_path", ["keys/0002.json", str(self.ws / "keys" / "0002.json")])
        self.expect(BLOCK, "Write", "file_path", ["keys/0001.json", "keys/notes.txt", "keys/sub/0002.json"])
        self.expect(ALLOW, "Write", "file_path", ["drafts/0002-key-v1.json"])

    def test_the_first_key_may_be_written_before_the_folder_exists(self):
        shutil.rmtree(self.ws / "keys")
        self.expect(ALLOW, "Write", "file_path", ["keys/0001.json"])


class SubagentTests(GuardCase):
    def test_the_grader_and_grade_reviewer_may_read_the_keys(self):
        for agent in ("grader", "grade-reviewer"):
            self.expect(ALLOW, "Read", "file_path", ["keys/0001.json", str(self.ws / "keys" / "0001.json")], agent=agent)
            self.expect(ALLOW, "Grep", "path", ["keys", "."], agent=agent)
            self.expect(ALLOW, "Glob", "pattern", ["keys/*"], agent=agent)

    def test_they_may_only_read(self):
        for agent in ("grader", "grade-reviewer"):
            self.expect(BLOCK, "Edit", "file_path", ["keys/0001.json"], agent=agent)
            self.expect(BLOCK, "Write", "file_path", ["keys/0001.json", "keys/0002.json"], agent=agent)
            self.expect(BLOCK, "Bash", "command", ["cat keys/0001.json"], agent=agent)

    def test_every_other_subagent_is_blocked(self):
        for agent in ("quiz-reviewer", "lesson-planner", "lesson-reviewer", "product-reviewer", "demo-dev",
                      "general-purpose", "Explore", "fork", "Grader", "grader-2"):
            self.expect(BLOCK, "Read", "file_path", ["keys/0001.json"], agent=agent)
            self.expect(BLOCK, "Grep", "path", ["."], agent=agent)
            self.expect(BLOCK, "Write", "file_path", ["keys/0002.json"], agent=agent)

    def test_an_allowed_name_without_an_agent_id_is_not_a_subagent(self):
        self.expect(BLOCK, "Read", "file_path", ["keys/0001.json"], agent="grader", agent_id=None)


class FailClosedTests(GuardCase):
    def test_input_it_cannot_understand_is_blocked(self):
        for stdin in ("", "not json", "[]", "null", "{}", '{"tool_name": "Read"}',
                      '{"tool_name": "Read", "tool_input": "keys"}', '{"tool_name": "Read", "tool_input": {}}',
                      '{"tool_name": "Read", "tool_input": {"file_path": "a\\u0000b"}}'):
            with self.subTest(stdin=stdin):
                self.assertEqual(self.run_guard(stdin).returncode, BLOCK)


class RegistrationTests(GuardCase):
    def setUp(self):
        super().setUp()
        self.settings = json.loads((TUTOR / ".claude" / "settings.json").read_text())
        [self.entry] = self.settings["hooks"]["PreToolUse"]
        [self.hook] = self.entry["hooks"]

    def test_it_covers_the_tools_and_blocks_when_it_fails(self):
        covered = set(self.entry["matcher"].split("|"))
        self.assertLessEqual({"Read", "Grep", "Glob", "Bash", "PowerShell", "Monitor", "Edit", "Write", "Skill"}, covered)
        self.assertEqual(self.hook["onFailure"], "block")

    def test_no_deny_rule_locks_the_grader_out(self):
        self.assertEqual([r for r in self.settings["permissions"]["deny"] if "keys" in r], [])

    @unittest.skipIf(os.name == "nt", "the registered command is for macOS and Linux")
    def test_the_registered_command_runs_the_script(self):
        env = {**os.environ, "CLAUDE_PROJECT_DIR": str(self.ws)}
        for path, code in (("keys/0001.json", BLOCK), ("MISSION.md", ALLOW)):
            data = {"tool_name": "Read", "tool_input": {"file_path": path}, "cwd": str(self.ws)}
            result = subprocess.run(self.hook["command"], shell=True, input=json.dumps(data), env=env,
                                    cwd=self.base, capture_output=True, text=True, timeout=20)
            self.assertEqual(result.returncode, code, result.stderr)
            if code == BLOCK:
                self.assertIn("keys guard: blocked", result.stderr)  # python also exits 2 for a missing script


if __name__ == "__main__":
    unittest.main()
