# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from webcaseland.models import Product, Category, SubCategory, Slider, Collection
from django.db.models import Q

admin.site.site_header = 'Administración de Caseland'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_pic','category','subcategory', 'order', 'visible')
    list_editable = ('order', 'visible','subcategory', 'order')
    list_filter = ('category', 'visible', 'visible', 'price')
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

    def get_queryset(self, request):
        qs = super(CategoryAdmin, self).get_queryset(request)
        return qs.filter(visible=True).exclude(name__iexact='Rincon del Hincha').exclude(name__iexact='Zona friki')\
            .exclude(name__iexact='Regalos').exclude(name__iexact='Promociones').order_by('order')


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'visible')
    list_editable = ('order', 'visible')
    ordering = ('order',)
    inlines = [ProductInline, SubCategoryInline]

    def get_queryset(self, request):
        qs = super(CollectionAdmin, self).get_queryset(request)
        return qs.filter(Q(visible=True) & (Q(name__iexact='Rincon del Hincha') | Q(name__iexact='Regalos') | Q(name__iexact='Zona friki')))


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
