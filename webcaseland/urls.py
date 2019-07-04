"""caseland URL Configuration"""

from django.conf.urls import url

from webcaseland import views
from webcaseland.views import ProductDetailView, ProductListView, SubCategoryListView, CatalogProductListView, \
    CatalogProductDetailView

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^product_detail/(?P<pk>.+)/$', ProductDetailView.as_view(), name="product_detail"),
    url(r'^catalog_product_detail/(?P<pk>.+)/$', CatalogProductDetailView.as_view(), name="catalog_product_detail"),
    url(r'^list_subcategory/([\w-]+)/$', SubCategoryListView.as_view(), name="list_subcategory"),
    url(r'^list_product/([\w-]+)/$', ProductListView.as_view(), name="list_product"),
    url(r'^list_catalog_product/([\w-]+)/$', CatalogProductListView.as_view(), name="list_catalog_product"),
]
