#!/usr/bin/env python3
"""Export the Ansible course into a deterministic, non-executable website bundle.

The Markdown and YAML files remain the only editable course content.
Requires Python 3.10+ and no third-party dependencies.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "mehrdad-dd/ansible_intro"
DIRECTORY_RE = re.compile(r"^([1-9][0-9]*)(?:st|nd|rd|th)_day$")
CODE_SUFFIXES = frozenset({".yml", ".yaml", ".ini", ".j2", ".py", ".cfg"})
MAX_FILE_BYTES = 256_000
FENCE = chr(96) * 3


def digest(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def text_file(root: Path, path: Path) -> str:
    """Read a file only if it is an ordinary file inside the source checkout."""
    resolved = path.resolve(strict=True)
    if not resolved.is_relative_to(root) or not path.is_file() or path.is_symlink():
        raise ValueError(f"Unsafe source path: {path}")
    if path.stat().st_size > MAX_FILE_BYTES:
        raise ValueError(f"Source file is too large: {path}")
    return path.read_text(encoding="utf-8")


def doc_paths(directory: Path, day: int) -> tuple[Path, Path, Path]:
    if day in (1, 2):
        return (
            directory / f"{directory.name}_Persian.md",
            directory / f"{directory.name}_English.md",
            directory / "playbook.yml",
        )
    if day == 3:
        return directory / "README.md", directory / "README_EN.md", directory / "user-security.yml"
    if day == 4:
        return (
            directory / "README.md",
            directory / "README_EN.md",
            directory / "ansible-roles-demo/playbooks/site.yml",
        )
    return directory / "README.md", directory / "README_EN.md", directory / "playbook.yml"


def heading(markdown: str) -> str:
    title = next((line[2:].strip() for line in markdown.splitlines()
                  if line.startswith("# ")), "")
    if not title:
        raise ValueError("Each localized lesson must have a level-one heading.")
    return title


def embedded_yaml(markdown: str) -> list[str]:
    pattern = re.compile(r"(?ms)^" + FENCE + r"yaml\n(.*?)\n" + FENCE + r"[ \t]*$")
    return pattern.findall(markdown)


def git_revision(root: Path) -> str | None:
    try:
        completed = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "--verify", "HEAD"],
            capture_output=True, text=True, check=True, timeout=5,
        )
    except (OSError, subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return None
    revision = completed.stdout.strip()
    return revision if re.fullmatch(r"[0-9a-f]{40}", revision) else None


def export_bundle(root: Path = ROOT, revision: str | None = None) -> dict:
    root = root.resolve(strict=True)
    license_text = text_file(root, root / "LICENSE")
    if not license_text.startswith("MIT License\n"):
        raise ValueError("Unexpected license: website publication requires a rights review.")

    directories = []
    for path in root.iterdir():
        if not path.is_dir() or path.is_symlink():
            continue
        found = DIRECTORY_RE.fullmatch(path.name)
        if found:
            directories.append((int(found.group(1)), path))
    directories.sort()
    days = [day for day, _ in directories]
    if not days or days != list(range(1, len(days) + 1)) or len(days) < 20:
        raise ValueError("The lesson directory sequence is incomplete.")

    lessons = []
    for day, directory in directories:
        fa_path, en_path, playbook_path = doc_paths(directory, day)
        fa = text_file(root, fa_path)
        en = text_file(root, en_path)
        playbook = text_file(root, playbook_path)
        code_fa, code_en = embedded_yaml(fa), embedded_yaml(en)
        if (len(code_fa) != 1 or code_fa != code_en
                or code_fa[0].strip() != playbook.strip()):
            raise ValueError(f"Day {day}: localized YAML must match the executable playbook.")

        asset_files = []
        for asset_path in sorted(directory.rglob("*")):
            if not asset_path.is_file() or asset_path.suffix not in CODE_SUFFIXES:
                continue
            if any(part.startswith(".") for part in asset_path.relative_to(directory).parts):
                continue
            content = text_file(root, asset_path)
            asset_files.append({
                "path": asset_path.relative_to(root).as_posix(),
                "content": content,
                "sha256": digest(content),
                "language": {
                    ".yml": "yaml", ".yaml": "yaml", ".j2": "jinja2",
                    ".py": "python", ".ini": "ini", ".cfg": "ini",
                }[asset_path.suffix],
            })

        lessons.append({
            "day": day,
            "slug": f"day-{day:02d}",
            "risk": "privileged-lab" if day <= 4 else "local-training",
            "translations": {
                "fa": {
                    "title": heading(fa),
                    "markdown": fa,
                    "sourcePath": fa_path.relative_to(root).as_posix(),
                },
                "en": {
                    "title": heading(en),
                    "markdown": en,
                    "sourcePath": en_path.relative_to(root).as_posix(),
                },
            },
            "playbookPath": playbook_path.relative_to(root).as_posix(),
            "files": asset_files,
        })

    content_hash = digest(json.dumps(lessons, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
    version = revision if revision is not None else git_revision(root)
    if version is not None and not re.fullmatch(r"[0-9a-f]{40}", version):
        raise ValueError("Source revision must be a 40-character commit SHA.")
    return {
        "schemaVersion": 1,
        "courseId": "ansible-intro",
        "locales": ["fa", "en"],
        "lessonCount": len(lessons),
        "contentSha256": content_hash,
        "source": {
            "repository": REPOSITORY,
            "revision": version,
            "license": "MIT",
            "licenseUrl": f"https://github.com/{REPOSITORY}/blob/main/LICENSE",
        },
        "lessons": lessons,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="-", help="File path; '-' prints JSON to stdout.")
    parser.add_argument("--revision", default=None, help="Optional exact 40-hex source commit.")
    args = parser.parse_args()
    try:
        bundle = export_bundle(revision=args.revision)
    except (OSError, UnicodeError, ValueError) as exc:
        parser.exit(1, f"Website export failed: {exc}\n")
    content = json.dumps(bundle, ensure_ascii=False, indent=2) + "\n"
    if args.output == "-":
        sys.stdout.write(content)
    else:
        target = Path(args.output)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        print(f"Exported {bundle['lessonCount']} lessons: {target}")


if __name__ == "__main__":
    main()
