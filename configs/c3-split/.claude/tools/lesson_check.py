"""Measure a lesson draft for the lesson-reviewer: reading time per section, and the demo scripts.

Usage: python3 .claude/tools/lesson_check.py <lesson.html>

Reading time is visible words / 150, the rule FORMATS.md says the bench uses: text inside
<script> and <style> is not counted. Words are split by <h2> headings, so each section's
measured minutes can be set beside the minutes its heading claims. Each inline <script> is
checked for syntax with node when node is installed, and every id or class the script looks up
is checked against the page. Standard library only; it reads the file and changes nothing.
"""

import re
import shutil
import subprocess
import sys
from html.parser import HTMLParser

WPM = 150
NOT_SHOWN = {"script", "style", "head", "template"}
LOOKUPS = re.compile(
    r"""getElementById\(\s*['"]([\w-]+)['"]|querySelector(?:All)?\(\s*['"]([^'"]+)['"]""")


def words_in(text):
    return sum(1 for t in text.split() if any(c.isalnum() for c in t))


class Lesson(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.meta, self.ids, self.classes, self.scripts = {}, set(), set(), []
        self.hidden = []                    # open tags whose text is not shown
        self.sections = [["(before the first heading)", "", []]]  # [heading, time label, text]
        self.in_h2 = self.in_time = False
        self.h2_text, self.time_text = [], []

    def handle_starttag(self, tag, attrs):
        a = {k: (v or "") for k, v in attrs}
        if tag == "meta" and a.get("name"):
            self.meta[a["name"].lower()] = a.get("content", "")
        if a.get("id"):
            self.ids.add(a["id"])
        self.classes.update(a.get("class", "").split())
        if tag in NOT_SHOWN:
            self.hidden.append(tag)
            if tag == "script" and not a.get("src"):
                self.scripts.append("")
        if tag == "h2" and not self.hidden:
            self.in_h2, self.h2_text, self.time_text = True, [], []
        if self.in_h2 and "section-time" in a.get("class", "").split():
            self.in_time = True

    def handle_endtag(self, tag):
        if self.hidden and tag == self.hidden[-1]:
            self.hidden.pop()
        if tag == "span":
            self.in_time = False
        if tag == "h2" and self.in_h2:
            self.in_h2 = False
            heading = " ".join("".join(self.h2_text).split())
            self.sections.append([heading, " ".join("".join(self.time_text).split()), [heading]])

    def handle_data(self, data):
        if self.hidden:
            if self.hidden[-1] == "script" and self.scripts:
                self.scripts[-1] += data
            return
        if self.in_h2:
            (self.time_text if self.in_time else self.h2_text).append(data)
        else:
            self.sections[-1][2].append(data)


def check_syntax(code):
    node = shutil.which("node")
    if not node:
        return "not checked (node is not installed)"
    probe = "new Function(require('fs').readFileSync(0, 'utf8'))"
    r = subprocess.run([node, "-e", probe], input=code, capture_output=True, text=True, timeout=30)
    if r.returncode == 0:
        return "ok"
    err = [line for line in r.stderr.splitlines() if "Error" in line]
    return "SYNTAX ERROR: " + (err[0].strip() if err else r.stderr.strip()[:200])


def missing_lookups(code, page):
    missing = []
    for by_id, selector in LOOKUPS.findall(code):
        if by_id and by_id not in page.ids:
            missing.append("#" + by_id)
        for kind, name in re.findall(r"([#.])([\w-]+)", selector or ""):
            if (kind == "#" and name not in page.ids) or (kind == "." and name not in page.classes):
                missing.append(kind + name)
    return sorted(set(missing))


def main(path):
    page = Lesson()
    with open(path, encoding="utf-8") as f:
        page.feed(f.read())
    page.close()

    asked = page.meta.get("p3-minutes", "")
    total = 0
    rows = []
    for heading, label, text in page.sections:
        n = words_in(" ".join(text))
        total += n
        if n or heading != page.sections[0][0]:
            rows.append((heading, label or "-", n))

    print(f"File: {path}")
    print(f"p3-minutes (requested): {asked or 'missing'}   p3-objective: {page.meta.get('p3-objective', 'missing')}")
    est = total / WPM
    ratio = f"{est / float(asked):.2f} of requested" if asked.replace('.', '', 1).isdigit() and float(asked) else "-"
    print(f"Visible words: {total}   Measured reading time: {est:.1f} min   ({ratio})")
    print()
    print("Section | Label | Words | Measured min")
    for heading, label, n in rows:
        title = re.sub(r"\s*\b\d+(\.\d+)?\s*min\b.*$", "", heading)[:70]
        print(f"{title} | {label} | {n} | {n / WPM:.1f}")
    print()
    if not page.scripts:
        print("Scripts: none")
    for i, code in enumerate(page.scripts, 1):
        lines = len(code.strip().splitlines())
        missing = missing_lookups(code, page)
        print(f"Script {i} ({lines} lines): syntax {check_syntax(code)}; "
              f"lookups not found in the page: {', '.join(missing) if missing else 'none'}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
