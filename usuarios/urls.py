from django.urls import path
from . import views
#from .views import menu_view

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registrar/', views.registrar, name='registrar'),
    path('iniciar-sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('menu/', views.menu, name='menu'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
]
