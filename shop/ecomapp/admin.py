# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin


from ecomapp.models import Category, Brand, Product, CartItem, Cart, Order

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

admin.site.register(Brand)

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Product, ProductAdmin)

admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Order)