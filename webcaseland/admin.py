# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from webcaseland.models import Product, Category, SubCategory, CatalogProduct

admin.site.site_header = 'Administración de Caseland'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'image_pic','category', 'order', 'visible')
    list_editable = ('order', 'visible')
    ordering = ('category__order', 'order', )

@admin.register(CatalogProduct)
class CatalogProductAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'image_pic','subcategory', 'order', 'visible')
    list_editable = ('order', 'visible')
    ordering = ('subcategory__order', 'order', )


class ProductInline(admin.TabularInline):
    model = Product
    extra = 0
    ordering = ('order',)

class CatalogProductInline(admin.TabularInline):
    model = CatalogProduct
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
    inlines = [CatalogProductInline]

