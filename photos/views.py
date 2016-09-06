from django.shortcuts import render
from photos.models import Photo


def home(request):
    """
    Renderiza el home con un listado de fotos
    :param request: objeto HttpRequest con los datos de la petición
    :return: objeto HttpResponse con los datos de la respuesta
    """
    photos = Photo.objects.all().order_by('-created_at')  # Acceso al ModelManager del modelo. Recupera todas las fotos de la base de datos
    context = {'photos_list': photos[:4]}

    return render(request, 'photos/home.html', context)
