from unittest import TestCase, mock

from django_pwa_courier import settings
from django_pwa_courier.views import ManifestView


class ManifestViewTest(TestCase):
    def test_init_sets_class_attribute(self):
        view = ManifestView()
        self.assertEqual(view.http_method_names, ["get", "options"])

    def test_get_returns_json_response_with_settings_manifest_as_data(self):
        view = ManifestView()
        with mock.patch("django_pwa_courier.views.manifest_view.JsonResponse") as mocked_json_response:
            view.get(request=None)

        mocked_json_response.assert_called_once_with(data=settings.PWA_MANIFEST)
