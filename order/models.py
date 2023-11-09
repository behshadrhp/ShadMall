from django.db import models
from django.conf import settings

from shop.models import Product


class Order(models.Model):
    '''
    This class is for ordering products.
    '''

    # initial information fields about customer
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)

    # stripe webhooks id
    stripe_id = models.CharField(max_length=250, blank=True)

    # create & update fields
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-create_at']
        indexes = [
            models.Index(fields=['-create_at'])
        ]

    def __str__(self) :
        return f'{self.first_name} - {self.last_name}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    
    def get_stripe_url(self):
        if not self.stripe_id:
            # no payment associated
            return ''
        if '__test__' in settings.STRIPE_SECRET_KEY:
            # stripe path for test payment
            path = '/test/'
        else:
            # stripe path for real payment
            path = '/'

        return f'https://dashboard.stripe.com{path}payments/{self.stripe_id}'


class OrderItem(models.Model):
    '''
    This class is for apply order item.
    '''

    # initial fields
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    # relationship with other models
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)

    
    def __str__(self):
        return f'{self.order} - {self.product}'
    
    def get_cost(self):
        return self.price * self.quantity
