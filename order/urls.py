from django.urls import path
from . import views


app_name = 'order'

urlpatterns = [
    path('create/', views.OrderCreate.as_view(), name='order_create'),
    path('/admin/order/<int:order_id>/pdf/', views.admin_order_export_to_pdf, name='admin_order_pdf'), 
]
