from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from photos.forms import PhotoForm
from photos.models import Photo, VISIBILITY_PUBLIC


def home(request):
    """
    Renderiza el home con un listado de fotos
    :param request: objeto HttpRequest con los datos de la petición
    :return: objeto HttpResponse con los datos de la respuesta
    """
    #photos = Photo.objects.all().order_by('-created_at')  # Acceso al ModelManager del modelo. Recupera todas las fotos de la base de datos
    photos = Photo.objects.filter(visibility=VISIBILITY_PUBLIC).order_by('-created_at')
    context = {'photos_list': photos[:4]} # Limita a las 4 últimas fotos

    return render(request, 'photos/home.html', context)


def photo_detail(request, pk):
    """
    Renderiza el detalle de una imagen
    :param request: objeto HttpRequest con los datos de la petición
    :para pk: Clave primaria de la foto a recuperar
    :return: objeto HttpResponse con los datos de la respuesta
    """
    possible_photos = Photo.objects.filter(pk=pk).select_related("owner")  # Obtiene las fotos y la relación con la tabla User
    if len(possible_photos) == 0:
        return HttpResponseNotFound("La imagen que buscas no existe")
    elif len(possible_photos) > 1:
        return HttpResponse("Múltiples opciones", status=300)

    photo = possible_photos[0]
    context = {'photo': photo}

    return render(request, 'photos/photo_detail.html', context)

def photo_creation(request):
    """
    Presenta el formulario para crear una foto y en caso de que la petición sea POST la valida y la crea en caso de que
    sea válida
    :param request: objeto HttpRequest con los datos de la petición
    :return: objeto HttpResponse con los datos de la respuesta
    """
    message = None
    if request.method == "POST":
        photo_with_user = Photo(owner=request.user)
        photo_form = PhotoForm(request.POST, instance=photo_with_user)
        if photo_form.is_valid():
            new_photo = photo_form.save()
            photo_form = PhotoForm()  # Pinta el formulario vacío en el siguiente renderizado
            message = 'Foto creada satisfactoriamente <a href="/photos/{0}">Ver foto</a>'.format(new_photo.pk)
    else:
        photo_form = PhotoForm()

    context = {'form': photo_form, 'message': message}
    return render(request, 'photos/photo_creation.html', context)