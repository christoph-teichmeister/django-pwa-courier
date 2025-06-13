from django.views import generic

from pwa_courier import constants


class HandleProtocolView(generic.TemplateView):
    template_name = "pwa_courier/pwa/handle_protocol.html"

    def get_context_data(self, **kwargs) -> dict:
        return {
            **super().get_context_data(**kwargs),
            "PWA_SANITIZED_WEB_PROTOCOL": constants.get_sanitised_pwa_web_protocol(),
        }
