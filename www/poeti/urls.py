from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_name', views.get_name, name='get_name'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)