# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic import DetailView, ListView
from django.db.models import Q

# Create your views here.
from webcaseland.models import Product, Category, SubCategory, Slider


def home(request):
    categories = Category.objects.filter(visible=True).exclude(name__iexact='Rincon del Hincha')\
        .exclude(name__iexact='Zona friki').exclude(name__iexact='Regalos').exclude(name__iexact='Promociones').order_by('order')
    corner_fan = SubCategory.objects.filter(visible=True, category__name__iexact='Rincon del Hincha').order_by('order')
    zona_friki = SubCategory.objects.filter(visible=True, category__name__iexact='Zona friki').order_by('order')
    gifts = SubCategory.objects.filter(visible=True, category__name__iexact='Regalos').order_by('order')

    collections = Category.objects.filter(Q(visible=True) & (Q(name__iexact='Rincon del Hincha') | Q(name__iexact='Regalos') | Q(name__iexact='Zona friki')))

    category_fan = Category.objects.filter(name__iexact='Rincon del Hincha').first()
    category_friki = Category.objects.filter(name__iexact='Zona friki').first()
    category_gift = Category.objects.filter(name__iexact='Regalos').first()
    category_promotion = Category.objects.filter(name__iexact='Promociones').first()
    sliders = Slider.objects.all().order_by('order')


    # models = ModelPhone.objects.filter(visible=True).order_by('brand__order','order')
    # slides = Slide.objects.filter(visible=True)

    return render_to_response('home.html', {'categories': categories, 'collections': collections, 'sliders': sliders,
                                            'cornerfan_list':corner_fan, 'friki_list': zona_friki,
                                            'gift_list': gifts,
                                            'category_fan': category_fan, 'category_friki': category_friki,
                                            'category_gift': category_gift, 'category_promotion': category_promotion })

class ProductDetailView(DetailView):
    model = Product
    template_name = 'detail-product.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(visible=True).exclude(name__iexact='Rincon del Hincha') \
            .exclude(name__iexact='Zona friki').exclude(name__iexact='Regalos').exclude(name__iexact='Promociones').order_by('order')
        context['collections'] = Category.objects.filter(Q(visible=True) & (Q(name__iexact='Rincon del Hincha') |
                                                                            Q(name__iexact='Regalos') |
                                                                            Q(name__iexact='Zona friki')))

        context['category_fan']= Category.objects.filter(name__iexact='Rincon del Hincha').first()
        context['category_friki'] = Category.objects.filter(name__iexact='Zona friki').first()
        context['category_gift'] =Category.objects.filter(name__iexact='Regalos').first()
        context['category_promotion'] = Category.objects.filter(name__iexact='Promociones').first()

        return context



class ProductListView(ListView):
    model = Category
    template_name = 'product.html'
    paginate_by = 40

    def get_queryset(self):
        type = self.kwargs['type']
        id = self.kwargs['id']
        if type=='category':
            category = get_object_or_404(Category, id=id)
            return Product.objects.filter(category=category, visible=True)
        elif type=='subcategory':
            category = get_object_or_404(Category, id=id)
            return SubCategory.objects.filter(category=category, visible=True)
        elif type == 'subcategory_catalog':
            subcategory = get_object_or_404(SubCategory, id=id)
            return Product.objects.filter(subcategory=subcategory, visible=True)


    def get_template_names(self):

        type = self.kwargs['type']

        if type == 'category':
            return ['product.html']
        elif type == 'subcategory_catalog':
            return ['catalog-product.html']
        elif type == 'subcategory':
            return ['subcategory-product.html']


    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(visible=True).exclude(name__iexact='Rincon del Hincha') \
            .exclude(name__iexact='Zona friki').exclude(name__iexact='Regalos').exclude(name__iexact='Promociones').order_by('order')
        context['collections'] = Category.objects.filter(Q(visible=True) & (Q(name__iexact='Rincon del Hincha') |
                                                                            Q(name__iexact='Regalos') |
                                                                            Q(name__iexact='Zona friki')))

        context['category_fan'] = Category.objects.filter(name__iexact='Rincon del Hincha').first()
        context['category_friki'] = Category.objects.filter(name__iexact='Zona friki').first()
        context['category_gift'] = Category.objects.filter(name__iexact='Regalos').first()
        context['category_promotion'] = Category.objects.filter(name__iexact='Promociones').first()

        return context


class SubCategoryListView(ListView):
    model = Category
    template_name = 'subcategory-product.html'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.args[0])
        return SubCategory.objects.filter(category=self.category, visible=True)

    def get_context_data(self, **kwargs):
        context = super(SubCategoryListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(visible=True).exclude(name__iexact='Rincon del Hincha') \
            .exclude(name__iexact='Zona friki').exclude(name__iexact='Regalos').exclude(name__iexact='Promociones').order_by('order')
        context['collections'] = Category.objects.filter(Q(visible=True) & (Q(name__iexact='Rincon del Hincha') |
                                                                            Q(name__iexact='Regalos') |
                                                                            Q(name__iexact='Zona friki')))

        context['category_fan'] = Category.objects.filter(name__iexact='Rincon del Hincha').first()
        context['category_friki'] = Category.objects.filter(name__iexact='Zona friki').first()
        context['category_gift'] = Category.objects.filter(name__iexact='Regalos').first()
        context['category_promotion'] = Category.objects.filter(name__iexact='Promociones').first()

        return context