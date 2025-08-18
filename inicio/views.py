from django.shortcuts import render

def home(request):
    return render(request, 'menu/home.html')

def base(request):
    return render(request, 'menu/base.html')

def servicios(request):
    return render(request, 'menu/servicios.html')

def galeria(request):
    return render(request, 'menu/galeria.html')

def contacto(request):
    if request.method == "POST":
        nombre = request.POST.get("name")
        correo = request.POST.get("email")
        telefono = request.POST.get("phone")
        servicio = request.POST.get("service")
        mensaje = request.POST.get("message")

        asunto = f"Nuevo mensaje de {nombre}"
        cuerpo = f"""
        Nombre: {nombre}
        Correo: {correo}
        Teléfono: {telefono}
        Servicio de interés: {servicio}

        Mensaje:
        {mensaje}
        """

        send_mail(
            asunto,                    # Asunto
            cuerpo,                    # Contenido del correo
            settings.EMAIL_HOST_USER,  # Siempre tu Gmail como remitente
            ["bachkatov.detailing@gmail.com"],    # Aquí pones tu Gmail (o varios correos si quieres)
            fail_silently=False,
        )

        return HttpResponse("Tu mensaje fue enviado con éxito ✅")

    return render(request, 'menu/contacto.html')


