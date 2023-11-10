import csv
import datetime

from django.urls import reverse
from django.http import HttpResponse
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Order, OrderItem


def order_payment(obj):
    url = obj.get_stripe_url()
    if obj.stripe_id:
        html = f'<a href="{url}" target="_blank">{obj.stripe_id}</a>'
        return mark_safe(html)
    return ''

order_payment.short_description = 'Stripe Payment'


def export_to_csv_file(admin_model, request, queryset):
    '''
    This function is for export data to csv file.
    '''

    opts = admin_model.model._meta
    content_disposition = f'attachment; filename={opts.verbose_name}.csv'
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = content_disposition
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    # write the first row with header information
    writer.writerow(
        [field.verbose_name for field in fields]
    )
    # write data rows 
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response

export_to_csv_file.short_description = 'Export To CSV'


def order_export_to_pdf_file(obj):
    url = reverse('order:admin_order_pdf', args=[obj.id])
    return mark_safe(f'<a href="{url}">PDF</a>')

order_export_to_pdf_file.short_description = 'Invoice'


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'email',
        'address',
        'postal_code',
        'city',
        'paid',
        order_payment,
        order_export_to_pdf_file
    ]

    list_filter = ['email', 'paid', 'create_at', 'update_at']
    ordering = ['-paid', '-create_at']
    inlines = [OrderItemInline]
    actions  = [export_to_csv_file]
