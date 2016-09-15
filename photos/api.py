from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from photos.models import Photo
from photos.serializers import PhotoSerializer, PhotoListSerializer


class PhotoListAPI(ListCreateAPIView):
    """
    Endpoint de listado y creación de fotos
    """
    queryset = Photo.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,) # Los usuarios no autenticados pueden ver fotos pero no crear

    def get_serializer_class(self):
        return PhotoSerializer if self.request.method == 'POST' else PhotoListSerializer

class PhotoDetailAPI(RetrieveUpdateDestroyAPIView):
    """
    Endpoint de detalle, actualización y borrado de fotos
    """
    queryset = Photo.objects.all()  # Devuelve un queryset con la consulta configurada (no ejecuta la consulta)
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)  # Los usuarios no autenticados pueden ver fotos pero no actualizar
