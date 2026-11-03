#!/usr/bin/env python3
"""Small dependency-free contract tests for the website JSON export."""
import hashlib
import json
from pathlib import Path
import re
import unittest

from export_website_content import ROOT, export_bundle

class WebsiteExportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = export_bundle(revision="a" * 40)

    def test_schema_and_all_locales(self):
        bundle = self.data
        self.assertEqual(bundle["schemaVersion"], 1)
        self.assertEqual(bundle["courseId"], "ansible-intro")
        self.assertEqual(bundle["locales"], ["fa", "en"])
        self.assertGreaterEqual(bundle["lessonCount"], 20)
        self.assertEqual([x["day"] for x in bundle["lessons"]], list(range(1, bundle["lessonCount"] + 1)))
        for lesson in bundle["lessons"]:
            self.assertEqual(set(lesson["translations"]), {"fa", "en"})
            self.assertRegex(lesson["slug"], r"^day-\d\d+$")
            for locale in ("fa", "en"):
                self.assertTrue(lesson["translations"][locale]["markdown"].startswith("# "))
            self.assertTrue(any(f["path"] == lesson["playbookPath"] for f in lesson["files"]))

    def test_source_code_integrity(self):
        for lesson in self.data["lessons"]:
            for asset in lesson["files"]:
                self.assertEqual(asset["sha256"], hashlib.sha256(asset["content"].encode()).hexdigest())
                self.assertEqual(asset["content"], (ROOT / asset["path"]).read_text(encoding="utf-8"))

    def test_deterministic_serialization(self):
        again = export_bundle(revision="a" * 40)
        self.assertEqual(self.data, again)
        self.assertEqual(
            json.dumps(self.data, ensure_ascii=False, sort_keys=True),
            json.dumps(again, ensure_ascii=False, sort_keys=True),
        )

    def test_no_executable_html_or_raw_site_changes(self):
        self.assertEqual(self.data["source"]["repository"], "mehrdad-dd/ansible_intro")
        self.assertEqual(self.data["source"]["license"], "MIT")
        self.assertTrue(re.fullmatch(r"[a-f0-9]{64}", self.data["contentSha256"]))


if __name__ == "__main__":
    unittest.main()
