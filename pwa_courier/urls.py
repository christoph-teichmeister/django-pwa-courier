from django.urls import path

from pwa_courier import views

app_name = "pwa_courier"

urlpatterns = [
    path("manifest.json", views.ManifestView.as_view(), name="manifest"),
    path("offline/", views.OfflineView.as_view(), name="offline"),
    path("handle-protocol/", views.HandleProtocolView.as_view(), name="handle_protocol"),
    path("serviceworker.js", views.ServiceWorkerView.as_view(), name="serviceworker"),
]
