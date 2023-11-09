from django.urls import path
from payment import views
from payment.webhooks import stripe_webhooks


app_name = 'payment'

urlpatterns = [
    path('process/', views.PaymentProcess.as_view(), name='process'),
    path('completed/', views.PaymentCompleted.as_view(), name='completed'),
    path('canceled/', views.PaymentCanceled.as_view(), name='canceled'),
    path('webhooks/', stripe_webhooks, name='stripe-webhooks'),
]
