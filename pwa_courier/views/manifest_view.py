import copy

from django.http import JsonResponse
from django.views import generic

from pwa_courier import settings


class ManifestView(generic.View):
    http_method_names = ("get", "options")

    def get(self, request, *args, **kwargs):
        manifest = copy.deepcopy(settings.get_pwa_manifest())
        if version := settings.get_pwa_icon_version():
            # Cache-bust icons so browsers fetch new images after they changed
            for icon in manifest.get("icons", []):
                icon["src"] = f"{icon['src']}?v={version}"

        response = JsonResponse(data=manifest, content_type="application/manifest+json")
        response["Cache-Control"] = "no-cache, must-revalidate"
        return response
