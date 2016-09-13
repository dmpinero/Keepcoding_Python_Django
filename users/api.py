from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from users.serializers import UserSerializer


class UserListAPI(APIView):
    """
    Endpoint de listado de usuarios
    """
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)  # Convierte lista de usuarios en lista de diccionarios
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)