from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='index'),
    path('galeria/', views.galeria, name='galeria'),
    path('servicios/', views.servicios, name='servicios'),
]
