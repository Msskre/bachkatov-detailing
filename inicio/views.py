from django.shortcuts import render

def menu(request):
    return render(request, 'menu/index.html')

def galeria(request):
    return render(request, 'menu/galeria.html')

def servicios(request):
    return render(request, 'menu/servicios.html')

