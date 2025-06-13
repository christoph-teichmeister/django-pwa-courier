from unittest import TestCase

from pwa_courier import settings
from pwa_courier.templatetags.pwa_tags import load_pwa_meta_data, load_serviceworker


class PWATagsTest(TestCase):
    def test_load_pwa_meta_data_returns_pwa_manifest_dict(self):
        self.assertEqual(load_pwa_meta_data(context=None), {"PWA_MANIFEST": settings.get_pwa_manifest()})

    def test_load_serviceworker_returns_relevant_dict(self):
        self.assertEqual(
            load_serviceworker(context=None),
            {
                "PWA_MANIFEST": settings.get_pwa_manifest(),
                "PWA_SERVICE_WORKER_DEBUG": settings.get_pwa_service_worker_debug(),
                "PWA_WEBPUSH_SETTINGS": settings.get_pwa_webpush_settings(),
            },
        )
