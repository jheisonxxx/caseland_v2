# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic import DetailView, ListView


# Create your views here.
from webcaseland.models import Product, Category


def home(request):
    categories = Category.objects.filter(visible=True).order_by('order')
    # models = ModelPhone.objects.filter(visible=True).order_by('brand__order','order')
    # slides = Slide.objects.filter(visible=True)
    return render_to_response('home.html', {'category_list': categories })

class ProductDetailView(DetailView):
    model = Product
    template_name = 'detail-product.html'


class ProductListView(ListView):
    model = Category
    template_name = 'product.html'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.args[0])
        return Product.objects.filter(category=self.category, visible=True)