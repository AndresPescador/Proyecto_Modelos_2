# todo/todo_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import *
from .serializers import TodoSerializer

class TodoListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # Get
    def get(self, request, *args, **kwargs):

        todos = Usuario.objects.filter(Usuario = request.ID_Usuario)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Post 
    def post(self, request, *args, **kwargs):

        data = {
            'Nombres': request.data.get('Nombres'), 
            'Apellidos': request.data.get('Apellidos'), 
            'Contrasena': request.data.get('Contrasena')
        }
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)