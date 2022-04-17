from django.contrib import admin
from . import models


class OrderLineItemAdminInline(admin.TabularInline):
    model = models.OrderLineItem
    readonly_fields = ('lineitem_total',)


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_id', 'date',
                       'total',)

    list_display = ('order_id', 'date', 'name',
                    'total',)
