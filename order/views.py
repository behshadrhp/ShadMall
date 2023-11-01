from django.views import View
from django.shortcuts import render

from .models import OrderItem
from .forms import OrderCerateForm
from cart.cart import Cart


class OrderCreate(View):
    '''
    This class is for create order products.
    '''

    def get(self, request):
        form = OrderCerateForm()
        cart = Cart(request)
        
        context = {'form': form, 'cart': cart}
        return render(request, 'order/create.html', context)

    def post(self, request):
        cart = Cart(request)
        form = OrderCerateForm(request.POST)

        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )

            # clear the cart
            cart.clear()
        
        context = {'order': order}
        return render(request, 'order/create.html', context)
