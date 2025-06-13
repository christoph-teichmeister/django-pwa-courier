[![PyPI release](https://img.shields.io/pypi/v/django-pwa-courier.svg)](https://pypi.org/project/django-pwa-courier/)
[![Downloads](https://static.pepy.tech/badge/django-pwa-courier)](https://pepy.tech/project/django-pwa-courier)
[![Coverage](https://img.shields.io/badge/Coverage-100.0%25-success)](https://github.com/christoph-teichmeister/django-pwa-courier/actions?workflow=CI)
[![Linting](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Coding Style](https://img.shields.io/badge/code%20style-Ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Documentation Status](https://readthedocs.org/projects/django-pwa-courier/badge/?version=latest)](https://django-pwa-courier.readthedocs.io/en/latest/?badge=latest)

Django-PWA-Courier transforms your Django app into a Progressive Web App
([PWA](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps)) and
delivers real-time push notifications to your users, all in one seamless package.

* [PyPI](https://pypi.org/project/django-pwa-courier/)
* [GitHub](https://github.com/christoph-teichmeister/django-pwa-courier)
* [Full documentation](https://django-pwa-courier.readthedocs.io/en/latest/index.html)
* Creator & Maintainer: [Chris Teichmeister](https://chris.teichmeister.lu/)

## Installation

- Install the package via pip:

  `pip install django-pwa-courier`

  or via pipenv:

  `pipenv install django-pwa-courier`

- Add module to `INSTALLED_APPS` within the main django `settings.py`:

```python
INSTALLED_APPS = (
    # ...
    "pwa_courier",
)
```

### Publish to ReadTheDocs.io

- Fetch the latest changes in GitHub mirror and push them
- Trigger new build at ReadTheDocs.io (follow instructions in admin panel at RTD) if the GitHub webhook is not yet set
  up.

### Publish to PyPi

- Update documentation about new/changed functionality

- Update the `Changelog`

- Increment version in main `__init__.py`

- Create pull request / merge to master

- This project uses the flit package to publish to PyPI. Thus, publishing should be as easy as running:
  ```
  flit publish
  ```

  To publish to TestPyPI use the following to ensure that you have set up your .pypirc as
  shown [here](https://flit.readthedocs.io/en/latest/upload.html#using-pypirc) and use the following command:

  ```
  flit publish --repository testpypi
  ```

### Maintenance

Please note that this package supports the [ambient-package-update](https://pypi.org/project/ambient-package-update/).
So you don't have to worry about the maintenance of this package. This updater is rendering all important
configuration and setup files. It works similar to well-known updaters like `pyupgrade` or `django-upgrade`.

To run an update, refer to the [documentation page](https://pypi.org/project/ambient-package-update/)
of the "ambient-package-update".
