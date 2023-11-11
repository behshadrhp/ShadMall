from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator


User = get_user_model()

class Coupon(models.Model):
    '''
    This class is for gift coupon.
    '''

    # initial information fields about coupon code
    code = models.CharField(max_length=50, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    active = models.BooleanField()
    discount = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ],
        help_text='Percentage value (0 to 100)'
    )
    

    # relationship with other models
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    # create & update fields
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-update_at', '-create_at']
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['code']),
            models.Index(fields=['valid_from', 'valid_to'])
        ]
    
    def __str__(self):
        return self.code
