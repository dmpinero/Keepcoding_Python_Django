from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserSerializer


class UserListAPI(APIView):
    """
    Endpoint de listado de usuarios
    """
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)  # Convierte lista de usuarios en lista de diccionarios
        return Response(serializer.data)
