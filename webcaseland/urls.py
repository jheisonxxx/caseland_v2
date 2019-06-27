"""caseland URL Configuration"""

from django.conf.urls import url

from webcaseland import views
from webcaseland.views import ProductDetailView, ProductListView

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^product_detail/(?P<pk>.+)/$', ProductDetailView.as_view(), name="product_detail"),
    url(r'^list_product/([\w-]+)/$', ProductListView.as_view(), name="list_product"),
]
