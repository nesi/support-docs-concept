# NesI support documentation

[![Deploy to gh-pages](https://github.com/nesi/support-docs-concept/actions/workflows/deploy.yml/badge.svg?branch=main&event=deployment_status)](https://github.com/nesi/support-docs-concept/actions/workflows/deploy.yml)

This repository contains the sources files for the NeSI support documentation.

Rendered pages are visible at https://nesi.github.io/support-docs-concept/.

> **Warning**
This is a beta version and should **not** be considered as the official documentation.
The official documentation is accessible at https://support.nesi.org.nz.

## Structure

The repository is organised using the following folders:

- `checks` : scripts intended to be run by CI,
- `docs`: markdown files, structure determines categories and sections[^1],
- `docs/assets`: non-template related files, e.g. images,
- `overrides`: theme overides or extensions.

[^1]: A section or category can be replaced by an `index.md` file, this will replace the default nav with a page.

## Theme

We are using the [mkdocs material theme](https://squidfunk.github.io/mkdocs-material/).

## Migration

Migration of the Zendesk documentation is done using our [migration pipeline (NeSI internal GitLab](https://git.hpcf.nesi.org.nz/cwal219/migratedocs).

Any one off filters (e.g. don't need to be checked every time, just when converting from ZD) should go there.

## Contributing

See the [dedicated documentation](CONTRIBUTING.md).
