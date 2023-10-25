from django.shortcuts import render, get_object_or_404
from django.views import View

from shop.models import Product, Category
from cart.forms import CartAddProductForm


class ProductView(View):
    '''
    This class is for rendering list products page.
    '''

    def get(self, request, category_slug=None):
        category = None
        categories = Category.objects.all()
        products = Product.objects.filter(available=True)
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = Product.objects.filter(category=category)

        context = {'category': category, 'categories': categories, 'products': products}
        return render(request, 'shop/product/list.html', context)
    

class ProductDetailView(View):
    '''
    This class is for rendering product detail page.
    '''

    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug, available=True)
        cart_product_form = CartAddProductForm()

        context = {'product': product, 'cart_product_form': cart_product_form}
        return render(request, 'shop/product/detail.html', context)
