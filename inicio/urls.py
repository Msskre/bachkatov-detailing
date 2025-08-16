from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('servicios/', views.servicios, name='servicios'),
    path('galeria/', views.galeria, name='galeria'),
    path('contacto/', views.contacto, name='contacto'),
]
