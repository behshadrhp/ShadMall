from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import stripe

from order.models import Order



@csrf_exempt
def stripe_webhooks(request):
    '''
    This Function is for set Webhooks.
    send to stripe app.
    '''

    payload = request.body
    sig_header = request.META('HTTP_STRIPE_SIGNATURE')
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload,
            sig_header,
            settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as ve:
        # invalid Payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as error:
        # invalid signature
        return HttpResponse(status=400)
    
    if event.type == 'checkout.session.completed':
        session = event.data.object
        if session.mode == 'payment' and session.payment_status == 'paid':
            try:
                order = Order.objects.get(id=session.client_refresh_id)
            except Order.DoesNotExist:
                return HttpResponse(status=404)
            
            # mark order as paid 
            order.paid = True
            order.save()

    return HttpResponse(status=200)
