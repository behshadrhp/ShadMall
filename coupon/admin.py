from django.contrib import admin
from .models import Coupon



@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    '''
    This class is for managing Coupon code from admin panel.
    '''

    list_display = ['code', 'valid_from', 'valid_to', 'discount', 'active']
    list_filter = ['active', 'valid_from', 'valid_to']
    search_fields = ['code__icontains']
    fields = [
        'code',
        'valid_from',
        'valid_to',
        'discount',
        'active'
    ]

    def save_model(self, request, obj, form, change):
            # change owner field to owner requested
            obj.owner = request.user
            return super().save_model(request, obj, form, change)
