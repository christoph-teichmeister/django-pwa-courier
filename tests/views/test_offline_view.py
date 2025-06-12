from unittest import TestCase

from django_pwa_courier import settings
from django_pwa_courier.views import OfflineView


class OfflineViewTest(TestCase):
    def test_class_attributes(self):
        self.assertEqual(OfflineView.template_name, "django_pwa_courier/offline.html")

    def test_get_context_data_sets_pwa_manifest_id(self):
        context_data = OfflineView().get_context_data()

        self.assertEqual(context_data["PWA_MANIFEST_ID"], settings.PWA_MANIFEST_ID)
