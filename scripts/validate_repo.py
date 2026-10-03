"""Lightweight public-note checks; academic review remains a human decision.

Run from anywhere with: python scripts/validate_repo.py
Only the Python standard library is used.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
REFERENCES = (
    ROOT
    / "plugins"
    / "optimization-knowledge"
    / "skills"
    / "optimization-knowledge"
    / "references"
)

LINK = re.compile(r"!?\[[^\]\n]*\]\((<[^>]+>|[^)\s]+)(?:\s+['\"][^'\"]*['\"])?\)")
# Uppercase drive letters catch ordinary Windows paths; lowercase drives need a
# second component so LaTeX such as f:\mathbb or \\y is not mistaken for one.
WINDOWS_PATH = re.compile(
    r"(?<![\w\\])(?:[A-Z]:[\\/][^\\/\s$}]+|[a-z]:[\\/][^\\/\s$}]+[\\/]|\\\\[A-Za-z0-9._-]+[\\/][A-Za-z0-9._-]+(?:[\\/]|\b))"
)
HOME_PATH = re.compile(r"(?<![\w])/(?:Users|home)/[^/\s]+(?:/|\b)")
UUID = re.compile(r"(?i)\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b")
ASSUMPTION = re.compile(r"假设|条件|适用范围|assumption|condition", re.I)
CONCLUSION = re.compile(r"结论|定理|命题|结果|conclusion|theorem|result", re.I)
PLACEHOLDER = re.compile(r"^(?:TODO|TBD|待补|待定|未核实|example(?:\.com)?|<.*>)$", re.I)


def display(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def markdown_without_code_fences(content: str) -> str:
    """Ignore examples in fenced/inline code when checking local links."""
    output: list[str] = []
    fence: str | None = None
    for line in content.splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            run = marker.group(1)
            if fence is None:
                fence = run[0]
            elif run[0] == fence:
                fence = None
            continue
        if fence is None:
            output.append(re.sub(r"`[^`]*`", "", line))
    return "\n".join(output)


def check_link(path: Path, destination: str, errors: list[str]) -> None:
    destination = destination.strip("<>")
    if not destination:
        errors.append(f"{display(path)}: empty Markdown link")
        return
    if destination.startswith(("#", "//")):
        return
    parsed = urlsplit(destination)
    if parsed.scheme:
        return

    local = unquote(parsed.path)
    if not local:
        return
    target = (ROOT / local.lstrip("/") if local.startswith("/") else path.parent / local).resolve()
    try:
        target.relative_to(ROOT)
    except ValueError:
        errors.append(f"{display(path)}: link escapes repository: {destination}")
        return
    if not target.exists():
        errors.append(f"{display(path)}: broken local link: {destination}")


def frontmatter(path: Path, content: str, errors: list[str]) -> tuple[dict[str, str], str]:
    lines = content.lstrip("\ufeff").splitlines()
    if not lines or lines[0].strip() != "---":
        errors.append(f"{display(path)}: knowledge note needs YAML frontmatter")
        return {}, content
    try:
        end = next(i for i, line in enumerate(lines[1:], start=1) if line.strip() == "---")
    except StopIteration:
        errors.append(f"{display(path)}: frontmatter has no closing ---")
        return {}, content

    fields: dict[str, str] = {}
    for line in lines[1:end]:
        if not line or line[0].isspace() or line.lstrip().startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        if key in fields:
            errors.append(f"{display(path)}: duplicate frontmatter field: {key}")
        fields[key] = value.strip().strip("\"'")
    return fields, "\n".join(lines[end + 1 :])


def check_note(path: Path, content: str, errors: list[str]) -> None:
    fields, body = frontmatter(path, content, errors)
    for name in ("title", "source", "scope", "status"):
        value = fields.get(name, "").strip()
        if not value or PLACEHOLDER.fullmatch(value):
            errors.append(f"{display(path)}: missing or placeholder {name}")

    source = fields.get("source", "").strip()
    if source and (not source.startswith("https://") or "example.com" in source or "localhost" in source):
        errors.append(f"{display(path)}: source needs a real HTTPS link to the original work")
    if fields.get("status") and fields["status"] != "verified":
        errors.append(f"{display(path)}: public knowledge notes require status: verified")

    # These are deliberately broad: a reviewer checks the actual math and evidence.
    if body and not ASSUMPTION.search(body):
        errors.append(f"{display(path)}: explain assumptions or applicable conditions")
    if body and not CONCLUSION.search(body):
        errors.append(f"{display(path)}: state the checked conclusion or result")


def validate() -> list[str]:
    errors: list[str] = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix.lower() == ".pdf":
            errors.append(f"{display(path)}: link to the original PDF; do not commit it")
            continue
        if path.suffix.lower() != ".md":
            continue
        try:
            content = path.read_text(encoding="utf-8-sig")
        except UnicodeDecodeError:
            errors.append(f"{display(path)}: Markdown file is not UTF-8")
            continue

        for description, pattern in (
            ("private absolute path", WINDOWS_PATH),
            ("private home path", HOME_PATH),
            ("possible conversation ID or private UUID", UUID),
        ):
            if pattern.search(content):
                errors.append(f"{display(path)}: {description} found")

        for match in LINK.finditer(markdown_without_code_fences(content)):
            check_link(path, match.group(1), errors)

        if path.is_relative_to(REFERENCES) and path.name.lower() != "index.md":
            check_note(path, content, errors)
    return errors


if __name__ == "__main__":
    problems = validate()
    if problems:
        for problem in problems:
            print(f"ERROR: {problem}", file=sys.stderr)
        print(f"Validation failed: {len(problems)} issue(s).", file=sys.stderr)
        raise SystemExit(1)
    print("Validation passed: public note metadata, local links and privacy markers checked.")
