# Instantiatio / iEWR website

MkDocs Material website for <https://instantiatio.github.io/iEWR/>.
English is primary at `/iEWR/eng/`; Russian is at `/iEWR/ru/`. The project root
redirects to English. Both languages use identical paths, with equivalent-page
language links rendered in HTML. Each language has its own search index and UI.

The accepted **Blue Architecture / Formative Clarity** style uses a deep-blue
Home introduction, a pale-blue practical action and light reading pages.
`overrides/` extends Material rather than replacing its search, mobile drawer,
code-copy controls or localized navigation. `hooks.py` groups the Home content
for presentation without editing the Markdown. The build check compares the
rendered article's words and order with those sources.

Manrope is served locally; its OFL license and source hashes are in
`assets/fonts/`. No remote font service is required.

The owner-selected frame-and-sphere background is a generated image exported as
WebP in `assets/hero/`. Only Home uses it; CSS keeps the text zones quiet and
limits the mobile image band to360px. The original PNG and generation prompt
remain in the project's local visual-trial materials.

## Build and check

Use Python 3.14 in a virtual environment:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python build.py
.venv/bin/python check.py
```

`site/` is generated and is not committed. To preview at the production base path,
serve the repository root after making a temporary `iEWR` symlink to `website/site`,
or use any static server mounted at `/iEWR/`. Do not preview at `/` with a different
base path: the site deliberately uses the GitHub project URL.

The `website-pages` workflow builds and checks on pull requests, and publishes the
same checked artifact after a push to `main` affecting this directory or the
workflow. GitHub Pages must use the **GitHub Actions** publishing source.

## Content and attribution

`docs/eng/` and `docs/ru/` contain the accepted bilingual publication materials.
Edit corresponding pages together. Shared images and selected experiment evidence
are in `assets/`; the quotation experiment has an inspectable evidence package,
and GEO CRM links to its illustrated PDF report.
Do not copy raw project archives or private working records here.

Conceptual sources: the Instantiatio research programme’s texts. Technical descriptions: iEWR **7.0.6**, pinned in page
links. GEO CRM evidence identifies its separate **7.0.0** environment. Screenshots
show synthetic data and the current English CRM interface in both languages.

Authorship, source provenance and license links are on each language's About page.
The repository MIT license and separately attributed FPF / third-party terms are
preserved. MkDocs and Material for MkDocs retain their upstream licenses.

The website build does not modify, package or release the engineering environment.

## Analytics

`overrides/partials/analytics.html` contains the owner-supplied Plausible snippet.
It loads once per locale page; the redirect at the project root is not tracked.
The site-specific script currently enables pageviews, engagement, outbound link
clicks and file download clicks. Search terms and form contents are not sent by
site code. Localhost is excluded by the standard Plausible script.

Use `/iEWR/eng/try/` and `/iEWR/ru/try/` in page reports (or optional pageview
goals) to inspect the practical entry. PDFs and the local experiment ZIP appear
under `File Download`; the release ZIP on GitHub is an outbound link. These are
click measurements, not confirmations of completed downloads or iEWR use.
Tracking options are managed in the owner's Plausible account. No private API
keys are stored in this repository. To stop collection, remove the analytics
include from `overrides/main.html` and publish again; update the About notices.
