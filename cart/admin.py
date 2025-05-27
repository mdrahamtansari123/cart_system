from django.contrib import admin
from .models import Product, CartItem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'quantity', 'created_at']
    search_fields = ['name']
    list_filter = ['created_at']


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'total_quantity', 'total_price', 'added_at']
    search_fields = ['user__username', 'product__name']
    list_filter = ['added_at']
