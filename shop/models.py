from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

from utils.validator import english_character_regex


User = get_user_model()

class Product(models.Model):
    '''
    This class is for creating Product.
    '''

    # initial information fields about product
    cover = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True)
    title = models.CharField(max_length=200, unique=True, validators=[english_character_regex])
    slug = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    # relationship with other models
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', related_name='product_category', on_delete=models.CASCADE)

    # create & update fields
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-update_at', '-create_at']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['title']),
            models.Index(fields=['-update_at', '-create_at'])
        ]
    
    def save(self, *args, **kwargs):

        # Save the slug with the title input parameter
        if not self.slug or self.slug != self.title:
            self.slug = slugify(self.title, allow_unicode=True)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Category(models.Model):
    '''
    This class is for sorting and categorizing products.
    '''

    # initial fields
    label = models.CharField(max_length=200, unique=True, validators=[english_character_regex])
    slug = models.SlugField(max_length=200, unique=True)

    # relationship with other models
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['label']
        indexes = [
            models.Index(fields=['label'])
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def save(self, *args, **kwargs):

        # Save the slug with the label input parameter
        if not self.slug or self.slug != self.label:
            self.slug = slugify(self.label, allow_unicode=True)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.label
