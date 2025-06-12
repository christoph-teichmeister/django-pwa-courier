from unittest import TestCase

from django_pwa_courier import settings
from django_pwa_courier.templatetags.pwa_tags import load_pwa_meta_data, load_serviceworker


class PWATagsTest(TestCase):
    def test_load_pwa_meta_data_returns_pwa_manifest_dict(self):
        self.assertEqual(load_pwa_meta_data(context=None), {"PWA_MANIFEST": settings.PWA_MANIFEST})

    def test_load_serviceworker_returns_relevant_dict(self):
        self.assertEqual(
            load_serviceworker(context=None),
            {
                "PWA_MANIFEST": settings.PWA_MANIFEST,
                "PWA_SERVICE_WORKER_DEBUG": settings.PWA_SERVICE_WORKER_DEBUG,
                "PWA_WEBPUSH_SETTINGS": settings.PWA_WEBPUSH_SETTINGS,
            },
        )
