from django.urls import path
from . import views
from .views import exit

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns=[
    path('',views.inicio,name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('productos',views.productos,name='productos'),
    path('productos/crear',views.crear,name='crear'),
    path('productos/editar',views.editar,name='editar'),
    path('eliminar/<int:id>',views.eliminar,name='eliminar'),
    path('productos/editar/<int:id>',views.editar,name='editar'),
    path('logout', views.exit, name='exit'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)