#!/usr/bin/env python3
"""Check FA/EN lesson parity, links, and basic publication safety."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def day_folder(n: int) -> str:
    suffix = "th" if 11 <= n % 100 <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suffix}_day"


def lesson_paths(day: int):
    root = ROOT / day_folder(day)
    if day in (1, 2):
        return (
            root / f"{day_folder(day)}_{'English'}.md",
            root / f"{day_folder(day)}_{'Persian'}.md",
            root / "playbook.yml",
        )
    if day == 3:
        return root / "README_EN.md", root / "README.md", root / "user-security.yml"
    if day == 4:
        return (
            root / "README_EN.md",
            root / "README.md",
            root / "ansible-roles-demo/playbooks/site.yml",
        )
    return root / "README_EN.md", root / "README.md", root / "playbook.yml"


def snippets(text: str, language: str):
    return re.findall(r"(?ms)^\`\`\`" + re.escape(language) + r"\n(.*?)\n\`\`\`", text)


def validate_links(path: Path, text: str):
    errors = []
    for target in re.findall(r"!?(?:\[[^]]*\])\(([^)]+)\)", text):
        target = target.split("#", 1)[0].strip()
        if not target or target.startswith(("http://", "https://", "mailto:", "/")):
            continue
        if not (path.parent / target).exists():
            errors.append(f"{path.relative_to(ROOT)}: broken link {target}")
    return errors


def main():
    errors = []
    root_readme = (ROOT / "README.md").read_text(encoding="utf-8")
    paths = [
        ROOT / "README.md",
        ROOT / "CONTRIBUTING.md",
        ROOT / "SECURITY.md",
        ROOT / "docs/GLOSSARY.md",
    ]
    for day in range(1, 21):
        en, fa, play = lesson_paths(day)
        for path in (en, fa, play):
            if not path.is_file():
                errors.append(f"Missing: {path.relative_to(ROOT)}")
        if not all(path.is_file() for path in (en, fa, play)):
            continue
        en_text = en.read_text(encoding="utf-8")
        fa_text = fa.read_text(encoding="utf-8")
        expected = play.read_text(encoding="utf-8").strip()
        english = snippets(en_text, "yaml")
        persian = snippets(fa_text, "yaml")
        if len(english) != 1 or english != persian or english[0].strip() != expected:
            errors.append(f"Day {day}: FA/EN YAML examples must exactly equal the executable playbook")
        # All examples and command flags must remain identical across both languages.
        for kind in ("bash", "python", "ini", "jinja2"):
            if snippets(en_text, kind) != snippets(fa_text, kind):
                errors.append(f"Day {day}: {kind} examples differ between languages")
        if en_text == fa_text:
            errors.append(f"Day {day}: missing prose localization")
        for path in (en, fa):
            paths.append(path)
            errors.extend(validate_links(path, path.read_text(encoding="utf-8")))
        if en.relative_to(ROOT).as_posix() not in root_readme or fa.relative_to(ROOT).as_posix() not in root_readme:
            errors.append(f"Day {day}: missing link in course index")
    for path in paths[:4]:
        if path.exists():
            errors.extend(validate_links(path, path.read_text(encoding="utf-8")))
    # Reject secrets and unsafe SSH settings from tracked automation configuration.
    sensitive = [
        re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----"),
        re.compile(r"\b(?:ghp_|github_pat_)[A-Za-z0-9_]{20,}"),
        re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
        re.compile(r"(?im)^\s*host_key_checking\s*=\s*(?:false|no|0)\s*$"),
    ]
    for path in ROOT.rglob("*"):
        if ".venv" in path.parts or ".git" in path.parts:
            continue
        if not path.is_file() or path.suffix not in (".yml", ".yaml", ".ini", ".cfg", ".j2"):
            continue
        body = path.read_text(encoding="utf-8", errors="replace")
        for pattern in sensitive:
            if pattern.search(body):
                errors.append(f"{path.relative_to(ROOT)}: publication safety pattern detected")
    if errors:
        for error in errors:
            print("FAIL:", error, file=sys.stderr)
        raise SystemExit(1)
    print("PASS: 20 bilingual lessons, executable YAML parity, relative links, basic safety checks")


if __name__ == "__main__":
    main()
