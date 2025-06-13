from unittest import TestCase, mock
from unittest.mock import MagicMock

from django.views.generic import TemplateView

from pwa_courier import settings
from pwa_courier.views import ServiceWorkerView


class ServiceWorkerViewTest(TestCase):
    def test_class_attributes(self):
        self.assertEqual(ServiceWorkerView.template_name, "pwa_courier/pwa/serviceworker.js")
        self.assertEqual(ServiceWorkerView.content_type, "text/javascript")

    def test_dispatch_sets_headers_correctly(self):
        view = ServiceWorkerView()
        mocked_response = MagicMock(headers={})
        with mock.patch.object(TemplateView, "dispatch", return_value=mocked_response):
            response = view.dispatch(request=None)

        self.assertEqual(response.headers["Service-Worker-Allowed"], "/")
        self.assertEqual(response.headers["Cache-Control"], "no-cache, no-store, must-revalidate")
        self.assertEqual(response.headers["Pragma"], "no-cache")
        self.assertEqual(response.headers["Expires"], "0")

    def test_get_context_data_sets_pwa_manifest_id_and_pwa_cache_id(self):
        context_data = ServiceWorkerView().get_context_data()

        self.assertEqual(context_data["PWA_MANIFEST_ID"], settings.get_pwa_manifest_id())
        self.assertEqual(context_data["PWA_CACHE_VERSION"], settings.PWA_CACHE_VERSION)
