from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag("django_pwa_courier/pwa/load_meta_data.html", takes_context=True)
def load_pwa_meta_data(context):
    return {"PWA_MANIFEST": settings.PWA_MANIFEST}


@register.inclusion_tag("django_pwa_courier/pwa/load_serviceworker.html", takes_context=True)
def load_serviceworker(context):
    return {
        "PWA_MANIFEST": settings.PWA_MANIFEST,
        "PWA_SERVICE_WORKER_DEBUG": settings.PWA_SERVICE_WORKER_DEBUG,
        "PWA_WEBPUSH_SETTINGS": settings.PWA_WEBPUSH_SETTINGS,
    }
