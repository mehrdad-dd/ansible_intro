#!/usr/bin/env python3
"""Side-effect-free demonstration of the Ansible inventory JSON protocol."""
import json
import sys

HOSTS = ["demo1", "demo2"]


def main():
    if "--host" in sys.argv:
        print("{}")
        return
    data = {
        "lab": {"hosts": HOSTS},
        "_meta": {
            "hostvars": {host: {"ansible_connection": "local"} for host in HOSTS}
        },
    }
    print(json.dumps(data))


if __name__ == "__main__":
    main()
