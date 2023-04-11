# todo/todo_api/models.py
from django.db import models

class Usuario(models.Model):
    ID_Usuario = models.BigAutoField(primary_key=True)
    Nombres = models.CharField(max_length=15)
    Apellidos = models.CharField(max_length=15)
    Contrasena = models.CharField(max_length=20)

class Rol(models.Model):
    ID_Rol = models.BigAutoField(primary_key=True)
    Nombre = models.CharField(max_length=15)
    Otros_atributos = models.TextField()

class Permiso(models.Model):
    ID_Permiso = models.BigAutoField(primary_key=True)
    Descripcion = models.TextField()

class Relacion_Usuario_Rol(models.Model):
    ID_Usuario = models.ManyToManyField(Usuario)
    ID_Rol = models.ManyToManyField(Rol)

class Relacion_Rol_Permiso(models.Model):
    ID_Rol = models.ManyToManyField(Rol)
    ID_Permiso = models.ManyToManyField(Permiso)