from django.contrib import admin

from pwa_courier.models import PushSubscription


@admin.register(PushSubscription)
class PushSubscriptionAdmin(admin.ModelAdmin):
    list_display = ("__str__", "browser", "user", "last_confirmed_at", "created_at")
    search_fields = ("user__email",)
    readonly_fields = ("user", "browser", "user_agent", "endpoint", "auth", "p256dh", "last_confirmed_at", "created_at")

    def has_add_permission(self, request):
        return False
