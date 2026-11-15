from django.urls import NoReverseMatch, reverse
from django.views import generic

from pwa_courier import settings


class ServiceWorkerView(generic.TemplateView):
    content_type = "text/javascript"

    def get_template_names(self):
        return [settings.get_pwa_service_worker_template()]

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        response.headers["Service-Worker-Allowed"] = "/"
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        return response

    def get_context_data(self, **kwargs) -> dict:
        try:
            admin_url = reverse("admin:index")
        except NoReverseMatch:
            admin_url = ""
        manifest = settings.get_pwa_manifest()
        return {
            **super().get_context_data(**kwargs),
            "PWA_MANIFEST": manifest,
            "PWA_CACHE_PREFIX": f"{manifest.get('short_name') or manifest.get('name') or 'pwa'}-cache-",
            "PWA_CACHE_VERSION": settings.get_pwa_cache_version(),
            "PWA_ADMIN_URL": admin_url,
        }
