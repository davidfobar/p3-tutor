"""The tutor's guard: a PreToolUse hook that keeps the answer keys in keys/ from being read.

Who may read keys/, with Read, Grep or Glob, and why:
- grade-reviewer: it checks each verdict and misconception id against the key.
- grader: the subagent that is to do the grading, which cannot be done without the key.
No one else may, not the main conversation and not any other subagent (quiz-reviewer reads the
draft key in drafts/). An allowed name counts only with an agent_id, so only inside a subagent.

What everyone else meets:
- Read, Edit, Write, NotebookEdit: no path in keys/, by any spelling or link. One exception: the
  main conversation may Write a key that does not exist yet, because /quiz has to create it.
- Grep: no path in keys/ and no folder that holds it, since a search prints what it finds. A
  search has to name a folder or file, such as lessons/.
- Glob: no pattern that names keys/. A general listing such as **/* passes: it gives names only.
- Bash, Monitor: an allowlist, because a shell can build a path in too many ways to list. It is
  the lesson checker, ls, find by name, pwd, date, echo and sleep, with no expansion or redirect.
- PowerShell: nothing.
- CLAUDE.md, CLAUDE.local.md: no writes, because an @keys/... line in one pastes the key into
  every later session without a Read call.
- Skill: no @-mention of keys in the arguments, because Claude Code pastes a mentioned file into
  the conversation without a Read call.

One gap it cannot close: an @-mention of a key that the learner types in their own message is
pasted in with no tool call, so no PreToolUse hook sees it.

Exit 0 allows the call and exit 2 blocks it. Input the guard cannot understand is blocked.
Registered in .claude/settings.json; tested by tests/test_guard.py in the repo.
"""

import fnmatch
import json
import os
import re
import shlex
import sys

KEY_READERS = {"grade-reviewer", "grader"}
MEMORY_FILES = {"claude.md", "claude.local.md"}
READ_TOOLS = {"Read", "Grep", "Glob"}
FILE_TOOLS = {"Read": "file_path", "Edit": "file_path", "MultiEdit": "file_path",
              "Write": "file_path", "NotebookEdit": "notebook_path"}

# the workspace root: this file is <root>/.claude/hooks/keys_guard.py
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
CHECKER = os.path.join(ROOT, ".claude", "tools", "lesson_check.py")

QUOTED = r"'[^']*'|\"[^\"$`\\]*\""
QUIET = r"(?<=\s)2>(?:\s*/dev/null|&1)(?=[\s;&|]|$)"
EXPANDS = re.compile(r"[$`\\*?\[\]{}~<>()#\n\r'\"]")
FIND_WITH_VALUE = {"-name", "-iname", "-type", "-maxdepth", "-mindepth"}
FIND_ALONE = {"-print", "-not", "!", "-o", "-a"}

NO_KEYS = ("keys/ holds the answer keys, and only the grade-reviewer and grader subagents may read them. "
           "Do not look for another way in and do not ask a subagent to quote a key: carry on without it.")
NO_MEMORY = "CLAUDE.md belongs to the tutor's author. Put what you learned about the learner in NOTES.md."
NARROW = ("a search there would reach the answer keys in keys/. "
          "Run it again on one folder or file, such as lessons/, quizzes/ or NOTES.md.")
NO_SHELL = ("the shell is limited here, so that it cannot reach keys/: use Read, Grep, Glob and Write instead. "
            "The shell may run only python3 .claude/tools/lesson_check.py <draft>, ls, find by name, "
            "pwd, date, echo and sleep, with no variables, unquoted wildcards or redirects.")


class Blocked(Exception):
    """The call may not run; the message says why and what to do instead."""


def is_keys(part):
    return part.split(":")[0].rstrip(". ").casefold() == "keys"


def inside(path, folder):
    path, folder = path.casefold(), folder.casefold()
    return path == folder or path.startswith(folder.rstrip(os.sep) + os.sep)


def spellings(path, cwd):
    """The path as written, tidied, and as the file system resolves it."""
    path = os.path.expanduser(str(path).strip().replace("\\", "/"))
    joined = os.path.join(cwd, path)
    return [os.path.normpath(joined), os.path.realpath(joined), os.path.realpath(os.path.normpath(joined))]


def in_keys(path, cwd):
    for full in spellings(path, cwd):
        if inside(full, os.path.realpath(os.path.join(ROOT, "keys"))):
            return True
        # only the part below the workspace counts, when there is one
        below = full[len(ROOT):] if inside(full, ROOT) else full
        if any(is_keys(p) for p in re.split(r"[/\\]", below)):
            return True
    return False


def names_keys(pattern):
    """Whether a name pattern singles out keys/: keys, k*ys or {lessons,keys}, but not * or **."""
    for part in re.split(r"[/\\,{}]", pattern.strip().replace(ROOT, "")):
        part = part.strip()
        if is_keys(part) or (part.strip("*") and fnmatch.fnmatch("keys", part.casefold())):
            return True
    return False


def check_file(tool, args, cwd, is_main):
    path = args.get(FILE_TOOLS[tool])
    if not isinstance(path, str) or not path.strip():
        raise Blocked("the call names no file.")
    if tool != "Read" and any(os.path.basename(p).rstrip(". ").casefold() in MEMORY_FILES for p in spellings(path, cwd)):
        raise Blocked(NO_MEMORY)
    if not in_keys(path, cwd):
        return
    if tool == "Write" and is_main:
        full = os.path.realpath(os.path.join(cwd, path))
        if os.path.dirname(full) == os.path.join(ROOT, "keys") and re.fullmatch(r"\d{4}\.json", os.path.basename(full)):
            if not os.path.lexists(full):
                return
            raise Blocked("that key exists, and a key is written once. Give a new quiz the next free number in quizzes/.")
    raise Blocked(NO_KEYS)


def check_grep(args, cwd):
    path = args.get("path") or "."
    if in_keys(path, cwd):
        raise Blocked(NO_KEYS)
    if names_keys(str(args.get("glob") or "")):
        raise Blocked(NO_KEYS)
    for full in spellings(path, cwd):
        holds_keys = inside(os.path.join(ROOT, "keys"), full)
        folder_outside = os.path.isdir(full) and not inside(full, ROOT)  # the repo around tutor/ holds keys too
        if holds_keys or folder_outside:
            raise Blocked(NARROW)


def check_glob(args, cwd):
    if in_keys(args.get("path") or ".", cwd) or names_keys(str(args.get("pattern") or "")):
        raise Blocked(NO_KEYS)


def check_find(words, cwd):
    words = iter(words)
    for word in words:
        if word in FIND_WITH_VALUE:
            if names_keys(next(words, "")):
                raise Blocked(NO_KEYS)
        elif word in FIND_ALONE:
            continue
        elif word.startswith("-"):
            raise Blocked(NO_SHELL)  # -exec, -files0-from and the like
        elif in_keys(word, cwd):
            raise Blocked(NO_KEYS)


def check_command(words, cwd):
    name, rest = words[0], words[1:]
    if name in ("python3", "python") and len(rest) == 2:
        if os.path.realpath(os.path.join(cwd, rest[0])) != CHECKER:
            raise Blocked(NO_SHELL)
        if in_keys(rest[1], cwd):
            raise Blocked(NO_KEYS)
    elif name == "ls":
        if any(in_keys(w, cwd) for w in rest if not w.startswith("-")):
            raise Blocked(NO_KEYS)
    elif name == "find":
        check_find(rest, cwd)
    elif name == "date":
        if not all(w.startswith("+") or w == "-u" for w in rest):
            raise Blocked(NO_SHELL)  # date -f prints the lines of a file
    elif name not in ("pwd", "echo", "sleep"):
        raise Blocked(NO_SHELL)


def check_shell(args, cwd):
    command = args.get("command")
    if not isinstance(command, str) or not command.strip():
        raise Blocked(NO_SHELL)
    # drop 2>/dev/null and 2>&1 where they stand outside quotes
    command = re.sub(f"{QUOTED}|{QUIET}", lambda m: "" if m.group().startswith("2>") else m.group(), command.strip())
    if EXPANDS.search(re.sub(QUOTED, "_", command)):
        raise Blocked(NO_SHELL)
    lexer = shlex.shlex(command, posix=True, punctuation_chars=";&|")
    lexer.whitespace_split = True
    lexer.commenters = ""
    words = []
    for word in [*lexer, ";"]:
        if word and set(word) <= set(";&|"):
            if word not in (";", "&&", "||", "|"):
                raise Blocked(NO_SHELL)
            if words:
                check_command(words, cwd)
            words = []
        else:
            words.append(word)


def check_skill(args):
    text = json.dumps(args).casefold()
    if "@" in text and "keys" in text:
        raise Blocked(NO_KEYS)


def check(data):
    tool, args = data["tool_name"], data["tool_input"]
    if not isinstance(tool, str) or not isinstance(args, dict):
        raise Blocked("the hook's input is not a tool call.")
    agent_id, agent = data.get("agent_id"), data.get("agent_type")
    if tool in READ_TOOLS and agent_id and agent in KEY_READERS:
        return
    cwd = data.get("cwd") or ROOT
    if tool in FILE_TOOLS:
        check_file(tool, args, cwd, is_main=not agent_id)
    elif tool == "Grep":
        check_grep(args, cwd)
    elif tool == "Glob":
        check_glob(args, cwd)
    elif tool in ("Bash", "Monitor"):
        check_shell(args, cwd)
    elif tool == "Skill":
        check_skill(args)
    elif tool == "PowerShell":
        raise Blocked(NO_SHELL)


def main():
    try:
        check(json.loads(sys.stdin.buffer.read()))
    except Blocked as exc:
        print(f"keys guard: blocked, {exc}", file=sys.stderr)
        return 2
    except Exception as exc:  # fail closed: a guard that crashes must not let the call through
        print(f"keys guard: blocked, the guard could not check this call ({type(exc).__name__}).", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
