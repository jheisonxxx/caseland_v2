from django.shortcuts import render, render_to_response


# Create your views here.

def home(request):
    # categories = Category.objects.filter(visible=True).order_by('order')
    # models = ModelPhone.objects.filter(visible=True).order_by('brand__order','order')
    # slides = Slide.objects.filter(visible=True)
    return render_to_response('home.html')

def product(request):
    # categories = Category.objects.filter(visible=True).order_by('order')
    # models = ModelPhone.objects.filter(visible=True).order_by('brand__order','order')
    # slides = Slide.objects.filter(visible=True)
    return render_to_response('product.html')

def detail_product(request):
    # categories = Category.objects.filter(visible=True).order_by('order')
    # models = ModelPhone.objects.filter(visible=True).order_by('brand__order','order')
    # slides = Slide.objects.filter(visible=True)
    return render_to_response('detail-product.html')