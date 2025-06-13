from django.views import generic

from pwa_courier import settings


class OfflineView(generic.TemplateView):
    template_name = "pwa_courier/offline.html"

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            "PWA_MANIFEST_ID": settings.get_pwa_manifest_id(),
        }
