"""caseland URL Configuration"""

from django.conf.urls import url

from webcaseland import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^product/$', views.product, name='product'),
    url(r'^detail_product/$', views.detail_product, name='detail-product'),
]
