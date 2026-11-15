from django.template import Context, Template


def _render(tag, **context):
    return Template("{% load pwa_tags %}{% " + tag + " %}").render(Context(context))


def test_pwa_meta_links_manifest_and_ios_tags(settings):
    settings.PWA_ICON_VERSION = 3

    html = _render("pwa_meta")

    assert 'href="/manifest.json"' in html
    assert 'name="apple-mobile-web-app-capable"' in html
    assert 'href="/static/icon-192.png?v=3" sizes="192x192"' in html


def test_pwa_serviceworker_passes_nonce_and_only_public_key(settings):
    settings.PWA_WEBPUSH = {**settings.PWA_WEBPUSH, "VAPID_PRIVATE_KEY": "secret-private"}

    html = _render("pwa_serviceworker", csp_nonce="n0nce")

    assert 'nonce="n0nce"' in html
    assert "PUBLICKEY" in html
    assert "secret-private" not in html
    assert "/push/subscribe/" in html
    assert "/serviceworker.js" in html


def test_pwa_ios_install_hint_renders_hidden_banner():
    html = _render("pwa_ios_install_hint")

    assert 'id="pwa-ios-install-hint" hidden' in html
    assert "Add to Home Screen" in html
