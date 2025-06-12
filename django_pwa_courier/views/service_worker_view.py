from django.views import generic

from django_pwa_courier import settings


class ServiceWorkerView(generic.TemplateView):
    template_name = "django_pwa_courier/pwa/serviceworker.js"
    content_type = "text/javascript"

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)

        response.headers["Service-Worker-Allowed"] = "/"
        # Add cache control headers
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"

        return response

    def get_context_data(self, **kwargs) -> dict:
        return {
            **super().get_context_data(**kwargs),
            "PWA_MANIFEST_ID": settings.PWA_MANIFEST_ID,
            "PWA_CACHE_VERSION": settings.PWA_CACHE_VERSION,
        }
