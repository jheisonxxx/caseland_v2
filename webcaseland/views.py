# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic import DetailView, ListView
from django.db.models import Q

# Create your views here.
from webcaseland.models import Product, Category, SubCategory, CatalogProduct


def home(request):
    categories = Category.objects.filter(visible=True).exclude(name__iexact='Rincon del Hincha')\
        .exclude(name__iexact='Zona friki').exclude(name__iexact='Regalos').order_by('order')
    corner_fan = SubCategory.objects.filter(visible=True, category__name__iexact='Rincon del Hincha').order_by('order')
    zona_friki = SubCategory.objects.filter(visible=True, category__name__iexact='Zona friki').order_by('order')
    gifts = SubCategory.objects.filter(visible=True, category__name__iexact='Regalos').order_by('order')

    collections = Category.objects.filter(Q(visible=True) & (Q(name__iexact='Rincon del Hincha') | Q(name__iexact='Regalos') | Q(name__iexact='Zona friki')))
    # models = ModelPhone.objects.filter(visible=True).order_by('brand__order','order')
    # slides = Slide.objects.filter(visible=True)
    return render_to_response('home.html', {'category_list': categories, 'cornerfan_list': corner_fan,
                              'gift_list': gifts ,'friki_list': zona_friki, 'collections': collections})

class ProductDetailView(DetailView):
    model = Product
    template_name = 'detail-product.html'

class CatalogProductDetailView(DetailView):
    model = CatalogProduct
    template_name = 'detail-product.html'


class ProductListView(ListView):
    model = Category
    template_name = 'product.html'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.args[0])
        return Product.objects.filter(category=self.category, visible=True)


class SubCategoryListView(ListView):
    model = Category
    template_name = 'subcategory-product.html'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.args[0])
        return SubCategory.objects.filter(category=self.category, visible=True)

class CatalogProductListView(ListView):
    model = SubCategory
    template_name = 'catalog-product.html'

    def get_queryset(self):
        self.subcategory = get_object_or_404(SubCategory, id=self.args[0])
        return CatalogProduct.objects.filter(subcategory=self.subcategory, visible=True)