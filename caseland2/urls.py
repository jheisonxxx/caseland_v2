"""caseland URL Configuration"""

from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static

from caseland2 import settings

urlpatterns = [
    url(r'^', include('webcaseland.urls', namespace='webcaseland')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)