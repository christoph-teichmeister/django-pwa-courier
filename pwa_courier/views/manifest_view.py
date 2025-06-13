from django.http import JsonResponse
from django.views import generic

from pwa_courier import settings


class ManifestView(generic.View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.http_method_names = ["get", "options"]

    def get(self, request, *args, **kwargs):
        return JsonResponse(data=settings.PWA_MANIFEST)
