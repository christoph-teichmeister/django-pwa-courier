from django import forms
from django.utils.timezone import now

from pwa_courier.models import PushSubscription
from pwa_courier.settings import user_wants_push


class PushSubscriptionForm(forms.ModelForm):
    status_type = forms.ChoiceField(choices=[("subscribe", "subscribe"), ("unsubscribe", "unsubscribe")])

    class Meta:
        model = PushSubscription
        fields = ("user", "browser", "user_agent", "endpoint", "auth", "p256dh", "status_type")

    def save_or_delete(self) -> None:
        data = dict(self.cleaned_data)
        status_type = data.pop("status_type")
        defaults = {"browser": data.pop("browser")}

        subscription, created = PushSubscription.objects.get_or_create(**data, defaults=defaults)

        if status_type == "unsubscribe" or not user_wants_push(data["user"]):
            subscription.delete()
            return

        # get_or_create() only saves on create, so bump re-confirmations explicitly to keep staleness detectable.
        if not created:
            subscription.last_confirmed_at = now()
            subscription.save(update_fields=["last_confirmed_at"])
