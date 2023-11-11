from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View

from .models import Coupon
from .forms import CouponApplyForm



class CouponApply(View):
    '''
    This class is for apply coupon.
    '''

    def post(self, request):
        now = timezone.now()
        form = CouponApplyForm(request.POST)
        
        if form.is_valid():
            try:
                coupon = Coupon.objects.get(
                    code__iexact=form['code'],
                    valid_from__lte=now,
                    valid_to__gte=now,
                    active=True
                )
                request.session['coupon_id'] = coupon.id
            except Coupon.DoesNotExist:
                request.session['coupon_id'] = None
        return redirect('cart:cart_detail')
