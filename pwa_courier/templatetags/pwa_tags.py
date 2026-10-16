from django import template

from pwa_courier import settings

register = template.Library()


def _nonce(context) -> str | None:
    # inclusion tags replace the parent context, so the CSP nonce must be passed through
    return context.get("csp_nonce") if context else None


@register.inclusion_tag("django_pwa_courier/pwa/load_meta_data.html", takes_context=True)
def pwa_meta(context):
    return {"PWA_MANIFEST": settings.get_pwa_manifest(), "PWA_ICON_VERSION": settings.get_pwa_icon_version()}


@register.inclusion_tag("django_pwa_courier/pwa/load_serviceworker.html", takes_context=True)
def pwa_serviceworker(context):
    webpush = settings.get_pwa_webpush_settings()
    return {
        "PWA_MANIFEST": settings.get_pwa_manifest(),
        "PWA_SERVICE_WORKER_DEBUG": settings.get_pwa_service_worker_debug(),
        # Only the public key goes to the browser
        "PWA_WEBPUSH": {"VAPID_PUBLIC_KEY": webpush["VAPID_PUBLIC_KEY"]},
        "csp_nonce": _nonce(context),
    }


@register.inclusion_tag("django_pwa_courier/pwa/ios_install_hint.html", takes_context=True)
def pwa_ios_install_hint(context):
    return {"PWA_MANIFEST": settings.get_pwa_manifest(), "csp_nonce": _nonce(context)}
