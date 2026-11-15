import http
import json

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from pwa_courier.forms import PushSubscriptionForm


@method_decorator(csrf_exempt, name="dispatch")
class PushSubscribeView(generic.View):
    """POST {status_type: subscribe|unsubscribe, subscription: PushSubscription.toJSON(), browser, user_agent}.

    201 subscribed, 202 unsubscribed, 400 invalid (JSON form errors), 401 not logged in.
    """

    http_method_names = ("post",)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponse(status=http.HTTPStatus.UNAUTHORIZED)

        try:
            data = json.loads(request.body.decode("utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            data = {}
        if not isinstance(data, dict):
            data = {}
        subscription = data.pop("subscription", None) or {}

        form = PushSubscriptionForm(
            data={
                **data,
                "endpoint": subscription.get("endpoint"),
                **subscription.get("keys", {}),
                "user": request.user.pk,
            }
        )
        if not form.is_valid():
            return HttpResponse(
                status=http.HTTPStatus.BAD_REQUEST,
                content_type="application/json",
                content=json.dumps(form.errors.get_json_data()),
            )

        form.save_or_delete()
        return HttpResponse(
            status=http.HTTPStatus.CREATED
            if form.cleaned_data["status_type"] == "subscribe"
            else http.HTTPStatus.ACCEPTED
        )
