from django import forms


class CouponApplyForm(forms.Form):
    '''
    This class is for Apply Coupon Code in Orders.
    '''

    code = forms.CharField(max_length=50)
