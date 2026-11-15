from django.views import generic

from pwa_courier import settings


class OfflineView(generic.TemplateView):
    template_name = "django_pwa_courier/pwa/offline.html"

    def get_context_data(self, **kwargs):
        return {**super().get_context_data(**kwargs), "PWA_MANIFEST": settings.get_pwa_manifest()}
