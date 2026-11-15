from django.conf import settings
from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


class PushSubscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="push_subscriptions", on_delete=models.CASCADE)

    browser = models.CharField(max_length=100)
    user_agent = models.CharField(max_length=500, blank=True)
    endpoint = models.URLField(max_length=500)
    auth = models.CharField(max_length=100)
    p256dh = models.CharField(max_length=100)

    # Last time the browser confirmed this subscription (initial subscribe or the silent re-subscribe on page load).
    # Not "last successful delivery": a long gap between pushes must not by itself look stale.
    last_confirmed_at = models.DateTimeField(_("Last confirmed at"), default=now)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)

    class Meta:
        verbose_name = _("Push subscription")
        verbose_name_plural = _("Push subscriptions")

    def __str__(self):
        return f"{self.user} ({self.browser})"
