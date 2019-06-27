# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from webcaseland.models import Product, Category

admin.site.site_header = 'Administración de Caseland'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'image_pic','category', 'order', 'visible')
    list_editable = ('order', 'visible')
    ordering = ('category__order', 'order', )


class ProductInline(admin.TabularInline):
    model = Product
    extra = 0
    ordering = ('order',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'color', 'visible')
    list_editable = ('order','color', 'visible')
    ordering = ('order',)
    inlines = [ProductInline]
