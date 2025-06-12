from unittest import TestCase

from django_pwa_courier import settings
from django_pwa_courier.views import HandleProtocolView


class HandleProtocolViewTest(TestCase):
    def test_class_attributes(self):
        self.assertEqual(HandleProtocolView.template_name, "django_pwa_courier/pwa/handle_protocol.html")

    def test_get_context_data_sets_pwa_sanitized_web_protocol(self):
        context_data = HandleProtocolView().get_context_data()

        self.assertEqual(context_data["PWA_SANITIZED_WEB_PROTOCOL"], settings.PWA_SANITIZED_WEB_PROTOCOL)
