from django.urls import path
from coupon import views


app_name = 'coupon'

urlpatterns = [
    path('apply/', views.CouponApply.as_view(), name='apply'),    
]
