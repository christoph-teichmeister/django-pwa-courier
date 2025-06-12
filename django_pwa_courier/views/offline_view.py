from django.conf import settings
from django.views import generic


class OfflineView(generic.TemplateView):
    template_name = "django_pwa_courier/offline.html"

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            "PWA_MANIFEST_ID": settings.PWA_MANIFEST_ID,
        }
