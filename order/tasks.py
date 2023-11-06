from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from celery import shared_task
from order.models import Order


@shared_task
def order_created(order_id):
    '''
    Task to send an e-mail notification when an order is
    successfully created.
    '''

    order = Order.objects.get(id=order_id)
    subject = f'order nr #{order.id}'
    message = f'Dear {order.first_name},\nYou have successfully placed an order.\nYour order ID is #{order.id}.'

    email = EmailMultiAlternatives(
        subject=subject,
        body=message,
        from_email=settings.DEFAULT_FROM_EMAIL, 
        to=[order.email],
    )

    return email
