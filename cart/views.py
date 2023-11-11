from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from shop.models import Product
from coupon.forms import CouponApplyForm
from .cart import Cart
from .forms import CartAddProductForm


class CartAddView(View):
    '''
    This class is for Add product to cart.
    '''

    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(
                product=product,
                quantity=cd['quantity'],
                override_quantity=cd['override']
            )
        return redirect('cart:cart_detail')


class CartRemoveView(View):
    '''
    This class is for remove the product on the shopping cart.
    '''

    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return redirect('cart:cart_detail')
    

class CartDetailView(View):
    '''
    This class is for review detail the shopping cart.
    '''

    def get(self, request):
        cart = Cart(request)
        coupon_apply_form = CouponApplyForm()

        context = {'cart': cart, 'coupon_apply_form': coupon_apply_form}
        return render(request, 'cart/detail.html', context)
