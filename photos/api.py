from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from photos.serializers import PhotoSerializer, PhotoListSerializer
from photos.views import PhotoQuerySet


class PhotoListAPI(ListCreateAPIView):
    """
    Endpoint de listado y creación de fotos
    """
    permission_classes = (IsAuthenticatedOrReadOnly,) # Los usuarios no autenticados pueden ver fotos pero no crear

    def get_serializer_class(self):
        return PhotoSerializer if self.request.method == 'POST' else PhotoListSerializer

    def get_queryset(self):
        return PhotoQuerySet.get_photos_by_user(self.request.user)

class PhotoDetailAPI(RetrieveUpdateDestroyAPIView):
    """
    Endpoint de detalle, actualización y borrado de fotos
    """
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)  # Los usuarios no autenticados pueden ver fotos pero no actualizar


    def get_queryset(self):
        return PhotoQuerySet.get_photos_by_user(self.request.user)
