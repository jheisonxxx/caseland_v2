# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from webcaseland.models import Product, Category, SubCategory, Slider

admin.site.site_header = 'Administración de Caseland'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_pic','category','subcategory', 'order', 'visible')
    list_editable = ('order', 'visible')
    ordering = ('category__order', 'order', )


class ProductInline(admin.TabularInline):
    model = Product
    extra = 0
    ordering = ('order',)


class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 0
    ordering = ('order',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'visible')
    list_editable = ('order', 'visible')
    ordering = ('order',)
    inlines = [ProductInline, SubCategoryInline]

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'visible')
    list_editable = ('order', 'visible')
    ordering = ('order',)
    inlines = [ProductInline]

admin.site.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'order',)
    list_editable = ('order',)
