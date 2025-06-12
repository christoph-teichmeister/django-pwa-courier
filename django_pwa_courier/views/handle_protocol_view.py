from django.views import generic

from django_pwa_courier import settings


class HandleProtocolView(generic.TemplateView):
    template_name = "django_pwa_courier/pwa/handle_protocol.html"

    def get_context_data(self, **kwargs) -> dict:
        return {
            **super().get_context_data(**kwargs),
            "PWA_SANITIZED_WEB_PROTOCOL": settings.PWA_SANITIZED_WEB_PROTOCOL,
        }
