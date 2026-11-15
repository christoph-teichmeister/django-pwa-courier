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

## Setup

```python
# urls.py: the service worker must be served from the root to control the whole site
urlpatterns = [path("", include("pwa_courier.urls")), ...]

# settings.py
PWA_MANIFEST = {
    "name": "My App",
    "short_name": "myapp",
    "scope": "/",
    "start_url": "/",
    "display": "standalone",
    "icons": [{"src": "/static/icon-192.png", "sizes": "192x192", "type": "image/png"}],
}
PWA_WEBPUSH = {
    "VAPID_PUBLIC_KEY": "...",
    "VAPID_PRIVATE_KEY": "...",
    "VAPID_ADMIN_EMAIL": "admin@example.com",
    "STALE_AFTER_DAYS": 10,
}
PWA_CACHE_VERSION = "1"  # bump (e.g. git commit) to drop old service worker caches
PWA_ICON_VERSION = 3  # optional, `?v=` on icons; or a dotted path to a callable
PWA_USER_WANTS_PUSH = "..."  # optional dotted path to callable(user) -> bool,
# default: user.wants_to_receive_webpush_notifications or True
PWA_SERVICE_WORKER_TEMPLATE = (
    "..."  # optional, your template that extends the package worker
)
PWA_SERVICE_WORKER_DEBUG = False
```

Run `python manage.py migrate`.

```django
{% load pwa_tags %}
<head>{% pwa_meta %}</head>
<body>
  ...
  <button onclick="pwaCourier.subscribe()">Enable notifications</button>
  {% pwa_ios_install_hint %}  {# optional banner: iOS only allows push from the home-screen app #}
  {% pwa_serviceworker %}     {# registers the worker, re-confirms subscriptions; CSP nonce is passed through #}
</body>
```

`pwaCourier.subscribe()` must run from a user gesture (iOS). It resolves to `true` when subscribed and fires a
`notificationsEnabled` event on `document`. `pwaCourier.unsubscribe()` removes the subscription.

### Sending

```python
from pwa_courier.notifications import Notification, has_only_stale_subscriptions

results = Notification(head="Hi", body="Tap to open", click_url="/inbox/").send_to(user)
Notification.was_delivered(results)  # any subscription accepted it
has_only_stale_subscriptions(
    user
)  # no subscription re-confirmed within STALE_AFTER_DAYS
```

Expired subscriptions (404/410) are deleted, other push errors are logged and return `False`.

### Service worker

The package worker precaches the offline page and manifest icons, serves pages network-first (cached copy, then
`/offline/` as fallback) and static files cache-first, shows pushes and handles notification clicks (focuses an open
window and redirects it, else opens one). Extend it:

```django
{% extends "django_pwa_courier/pwa/serviceworker.js" %}
{% block precache %}"/static/app.css",{% endblock %}
{% block fetch %}/* your own caching instead of the default */{% endblock %}
{% block extra %}/* additional listeners */{% endblock %}
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
