from rest_framework import serializers


class UserSerializer(serializers.Serializer):

    first_name = serializers.CharField()
    last_name = serializers.CharField()


    def create(self, validated_data):
        pass


    def update(self, instance, validated_data):
        pass
