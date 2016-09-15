from rest_framework import serializers

from photos.models import Photo


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo


class PhotoListSerializer(PhotoSerializer):

    class Meta(PhotoSerializer.Meta):
        fields = ('id', 'name', 'url')  # Campos a mostrar