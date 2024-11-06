from django.contrib import admin
from .models import Product, Order, OrderItem, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "stock", "prescription_required", "is_active"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "is_active"]


class OrderAdmin(admin.ModelAdmin):
    list_display = ["order_id", "total_amount", "status", "created_at", "updated_at"]


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["order", "product", "quantity", "price"]


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Category, CategoryAdmin)
