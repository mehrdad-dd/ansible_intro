# One-source Ansible website sync | همگام‌سازی آموزش با وب‌سایت

**Source of truth:** [mehrdad-dd/ansible_intro](https://github.com/mehrdad-dd/ansible_intro)  
**Consumer:** [mehrdad-dd/Project_Website_01](https://github.com/mehrdad-dd/Project_Website_01) (private React/Vite website).

## Contract / قرارداد

The course's Markdown, playbooks and lab files are edited **only here**. The website can check out this public repository at an exact Git commit and export all lessons into one deterministic JSON bundle:

```bash
python3 tools/export_website_content.py --output /tmp/ansible-content.v1.json
python3 -m unittest discover -s tools -p 'test_website_export.py' -v
```

The export is read-only. It **never** executes Ansible playbooks, installs packages, reads Vault passwords, or contacts a server. The build fails if a lesson or its counterpart is missing, or if FA/EN YAML differs from the executable playbook.

**Schema version 1:** `schemaVersion`, `courseId`, `source` (repository, exact SHA, MIT license), `lessonCount`, `contentSha256`, `locales`, and ordered `lessons`. Each lesson has a stable `slug`, `risk`, FA/EN `translations` (`title`, `markdown`, `sourcePath`), and local text `files` (including the executable playbook and SHA-256).

The JSON is generated, not hand-edited or committed to either source repository. The website caches its generated version within its build or a bot-created PR.

## Recommended website workflow / روش پیشنهادی

1. On a schedule or a manually triggered workflow **in the website repository**, check out the **website** and a **read-only** copy of `ansible_intro`, using `actions/checkout` with `repository: mehrdad-dd/ansible_intro` and a separate `path`.
2. Record the exact SHA (`git -C ... rev-parse HEAD`); optionally require a successful upstream CI check before accepting it.
3. Run the Python exporter in that checkout and validate `schemaVersion == 1`, all slugs, translations, source hashes and file sizes.
4. Convert the resulting JSON into the website's own **generated** content files. Never write to the source Markdown in the website. The existing route `/category/automation/ansible-playbooks` should remain a course landing page.
5. For each lesson, use an SEO-friendly route such as `/fa/ansible/day-01` and `/en/ansible/day-01`. Render Markdown safely without executing embedded HTML, scripts or YAML; keep code copyable.
6. Validate the website with `npm ci && npm run check`. Produce a change-only Pull Request. If no files changed, do nothing.
7. Do **not** automatically merge or trigger production deployment. Prefer human review for content and dependency updates.

### How to achieve one-place editing

When a lesson Markdown or playbook changes in this repository, the website's scheduled sync detects a changed `contentSha256` and refreshes its generated files. No one edits the generated copies manually. Source corrections naturally propagate into both FA/EN website pages after the website's tests and PR review.

## Security

- No cross-repository long-lived PAT is required to **read** this public repo. The website workflow's own limited token (or an approved GitHub App) may be needed to **create a website PR**; do not expose it to the browser.
- Pin third-party Actions to reviewed immutable commit SHAs. Use `permissions: contents: read` for read-only jobs; grant `contents: write` and `pull-requests: write` only to the PR writer job when configured.
- Never execute source playbooks on website build runners.
- Treat Markdown as **untrusted input**: disable raw HTML and unsafe URI schemes; use a sanitized Markdown renderer and strict link handling.
- Reject path traversal, symlinks, oversized files, unexpected document formats and unexpected schema versions.
- Code snippets are inert text. Mark lessons 1–4 as **privileged training labs**, not browser-executable exercises.
- Keep credit to the upstream content and include the repository MIT notice or link without asserting all third-party material is license-free.
- Avoid copying private credentials, operational inventories, `node_modules` or runtime logs.

## SEO and language

The website currently uses a client-side React/Vite router. For reliably indexable course pages, **pre-render or server-render** individual lesson URLs; merely adding dynamic meta tags in the browser does not guarantee crawlers see the full lesson. Include per-language `title`, `description`, canonical and `hreflang`, add all localized pages to `sitemap.xml`, and preserve the site's theme, RTL support and existing navigation.

The website has a German UI, but the source course is **FA/EN**. The German Ansible overview may link to these language editions; do not invent German translations or use an incorrect `hreflang=de` for English text.

### Non-goals

This source-side change **does not** modify or deploy the website, and does not claim live synchronization until the website consumer is implemented. It supplies the stable exporter, contract tests and documentation necessary for that next step.
