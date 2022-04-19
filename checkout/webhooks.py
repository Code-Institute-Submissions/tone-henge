import stripe
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .webhook_handler import StripeWH_Handler


@require_POST
@csrf_exempt
def webhook(request):
    """Listener for Stripe webhooks. Pass event to custom webhook handler."""

    wh_secret = settings.WH_SECRET
    stripe.api_key = settings.STRIPE_PRIVATE_KEY

    event = None
    payload = request.data

    if wh_secret:
        sig_header = request.headers.get('stripe-signature')
        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, wh_secret
            )
        except stripe.error.SignatureVerificationError as e:
            print('Webhook signature verification failed.' + str(e))
            return HttpResponse(status=400)

    handler = StripeWH_Handler(request)
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
    }
    event_type = event['type']
    event_handler = event_map.get(event_type, handler.handle_event)

    response = event_handler(event)
    return response
