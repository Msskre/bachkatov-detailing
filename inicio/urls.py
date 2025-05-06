from django.urls import path
from . import views
from django.http import JsonResponse

def ping(request):
    return JsonResponse({"status": "ok"})

urlpatterns = [
    path('ping/', ping, name='ping'),
    path('', views.menu, name='index'),
    path('galeria/', views.galeria, name='galeria'),
    path('servicios/', views.servicios, name='servicios'),
]
