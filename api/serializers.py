from django.db import models
from django.db.models import fields
from rest_framework import serializers
from bookstore.models import Autor, Libro

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nombre', 'creado_por', 'creado']

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ['id','titulo','descripcion','autor','creado_por', 'creado']
