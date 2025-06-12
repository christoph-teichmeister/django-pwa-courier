from unittest import TestCase

from django_pwa_courier.views import ManifestView


class ManifestViewTest(TestCase):
    def test_init_sets_class_attribute(self):
        view = ManifestView()
        self.assertEqual(view.http_method_names, ["get", "options"])
