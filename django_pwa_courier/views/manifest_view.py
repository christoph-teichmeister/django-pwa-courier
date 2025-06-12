from django.conf import settings
from django.http import JsonResponse
from django.views import generic


class ManifestView(generic.View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.http_method_names = ["get", "options"]

    def get(self, request, *args, **kwargs):
        return JsonResponse(data=settings.MANIFEST)
