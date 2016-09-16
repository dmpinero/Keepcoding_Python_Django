from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from photos.serializers import PhotoSerializer, PhotoListSerializer
from photos.views import PhotoQuerySet

class PhotoViewSet(ModelViewSet):
    """
    Endpoint de listado y creación de fotos
    """
    permission_classes = (IsAuthenticatedOrReadOnly,) # Los usuarios no autenticados pueden ver fotos pero no crear

    # Filtrado y Ordanación en la API
    search_fields = ('name', 'description')  # Campos por los que se realiza la búsqueda
    order_fields = ('owner', 'created_at', 'name', 'id')  # Campos de ordenación
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)  # Habilitar ordenación y filtrado en API

    def get_serializer_class(self):
        return PhotoSerializer if self.action != 'list' else PhotoListSerializer

    def get_queryset(self):
        return PhotoQuerySet.get_photos_by_user(self.request.user)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)  # El usuario propietario de la foto es el autenticado

    def perform_update(self, serializer):
        return serializer.save(owner=self.request.user)  # El usuario propietario de la foto es el autenticado