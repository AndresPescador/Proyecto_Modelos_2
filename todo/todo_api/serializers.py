# todo/todo_api/serializers.py
from rest_framework import serializers
from .models import *

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ["Nombres", "Apellidos", "Contrasena"]

        model = Rol
        fields = ["Nombre", "Otros_atributos"]

        model = Permiso
        fields = ["Nombre", "Descripcion"]