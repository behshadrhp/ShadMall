from django.conf import settings
from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.template.loader import render_to_string

import weasyprint

from .models import OrderItem, Order
from .forms import OrderCerateForm
from cart.cart import Cart
from .tasks import order_created


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

            # launch asynchronous task
            order_created.delay(order.id)
            # set the order in the session
            request.session['order_id'] = order.id
            # redirect for payment
            return redirect(reverse('payment:process'))
        
        context = {'order': order}
        return render(request, 'order/create.html', context)


@staff_member_required
def admin_order_export_to_pdf(request, order_id):
    '''
    this class is for export data to pdf file.
    '''

    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('export/pdf.html', {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
    weasyprint.HTML(string=html).write_pdf(response)

    return response
