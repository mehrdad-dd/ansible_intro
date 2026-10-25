#!/usr/bin/env python3
"""Syntax-check every lesson; smoke-test only safe, unprivileged localhost labs."""
import argparse
import os
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def day_folder(n):
    suffix = "th" if 11 <= n % 100 <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suffix}_day"


def command_for(day):
    folder = ROOT / day_folder(day)
    if day == 4:
        project = folder / "ansible-roles-demo"
        return project, ["ansible-playbook", "-i", "inventory/lab/hosts.yml", "playbooks/site.yml"]
    play = "user-security.yml" if day == 3 else "playbook.yml"
    inventory = "inventory.py" if day == 16 else "inventory.yml" if day >= 6 else "inventory.ini"
    if day == 3:
        inventory = "../2nd_day/inventory.ini"
    return folder, ["ansible-playbook", "-i", inventory, play]


def invoke(label, args, cwd, timeout=90):
    environment = dict(os.environ, ANSIBLE_NOCOLOR="1", ANSIBLE_RETRY_FILES_ENABLED="0")
    print(f"RUN {label}: {' '.join(args)}", flush=True)
    result = subprocess.run(
        args, cwd=cwd, env=environment, capture_output=True,
        text=True, timeout=timeout, check=False,
    )
    if result.returncode:
        print(result.stdout[-4000:])
        print(result.stderr[-4000:])
        raise SystemExit(f"FAIL {label}: exit {result.returncode}")
    return result.stdout


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--syntax", action="store_true")
    group.add_argument("--smoke", action="store_true")
    args = parser.parse_args()

    if args.syntax:
        days = range(1, 21)
        for day in days:
            cwd, command = command_for(day)
            invoke(f"day {day} syntax", command + ["--syntax-check"], cwd)
    else:
        # Days 1–4 deliberately manage system state. Never smoke-test those in CI.
        for day in range(6, 21):
            cwd, command = command_for(day)
            output = invoke(f"day {day} smoke", command, cwd)
            if "failed=0" not in output:
                raise SystemExit(f"FAIL day {day}: no successful play recap found")
            if day in (11, 19, 20):
                second = invoke(f"day {day} repeat", command, cwd)
                if not re.search(r"\bchanged=0\b", second):
                    raise SystemExit(f"FAIL day {day}: second run was not idempotent")
    print("PASS: all requested Ansible checks completed")


if __name__ == "__main__":
    main()
