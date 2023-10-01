from django.contrib import admin
from shop import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    '''
    This class is for managing products from admin panel.
    '''

    list_display = ['owner', 'title', 'category', 'price', 'available']
    list_filter = ['owner', 'category', 'available']
    search_fields = ['title__icontains', 'description__icontains', 'price__icontains']
    fields = ['cover', 'title', 'slug', 'description', 'price', 'category', 'available']
    readonly_fields = ['owner']
    list_per_page = 10
    prepopulated_fields = {
        'slug': ('title',)
    }

    def save_model(self, request, obj, form, change):
            # change owner field to owner requested
            obj.owner = request.user
            return super().save_model(request, obj, form, change)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    '''
    This class is for managing categories from admin panel.
    '''

    list_display = ['owner', 'label']
    fields = ['label', 'slug']
    readonly_fields = ['owner']
    list_per_page = 10
    prepopulated_fields = {
        'slug': ('label',)
    }

    def save_model(self, request, obj, form, change):
            # change owner field to owner requested
            obj.owner = request.user
            return super().save_model(request, obj, form, change)
