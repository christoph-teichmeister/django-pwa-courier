from django import template

from pwa_courier import settings

register = template.Library()


@register.inclusion_tag("pwa_courier/pwa/load_meta_data.html", takes_context=True)
def load_pwa_meta_data(context):
    return {"PWA_MANIFEST": settings.get_pwa_manifest()}


@register.inclusion_tag("pwa_courier/pwa/load_serviceworker.html", takes_context=True)
def load_serviceworker(context):
    return {
        "PWA_MANIFEST": settings.get_pwa_manifest(),
        "PWA_SERVICE_WORKER_DEBUG": settings.get_pwa_service_worker_debug(),
        "PWA_WEBPUSH_SETTINGS": settings.get_pwa_webpush_settings(),
    }
