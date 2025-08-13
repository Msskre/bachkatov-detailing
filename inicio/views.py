from django.shortcuts import render

def base(request):
    return render(request, 'menu/base.html')

def home(request):
    return render(request, 'menu/home.html')

def servicios(request):
    return render(request, 'menu/servicios.html')

def galeria(request):
    return render(request, 'menu/galeria.html')

def contacto(request):
    return render(request, 'menu/contacto.html')


