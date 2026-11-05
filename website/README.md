# Instantiatio / iEWR website

MkDocs Material website for <https://instantiatio.github.io/iEWR/>.
English is primary at `/iEWR/eng/`; Russian is at `/iEWR/ru/`. The project root
redirects to English. Both languages use identical paths, with equivalent-page
language links rendered in HTML. Each language has its own search index and UI.

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
are in `assets/`; public evidence ZIPs identify their sources and transformations.
Do not copy raw project archives or private working records here.

Conceptual sources: the Instantiatio research programme and
<https://t.me/instantiatio>. Technical descriptions: iEWR **7.0.6**, pinned in page
links. GEO CRM evidence identifies its separate **7.0.0** environment. Screenshots
show synthetic data and the current Russian CRM interface in both languages.

Authorship, source provenance and license links are on each language's About page.
The repository MIT license and separately attributed FPF / third-party terms are
preserved. MkDocs and Material for MkDocs retain their upstream licenses.

The website build does not modify, package or release the engineering environment.
