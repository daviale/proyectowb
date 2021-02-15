from rest_framework import serializers
from Tiendaonline.models import Rol, Direccion, Category, Product, List, Usuario, client

class RolSerializer(serializers.ModelSerializer):
    class Meta:
       model = Rol
       fields = ['id', 'nombre'] 
class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = ['id', 'nombre']     

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','nombre']    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','nombre', 'precio','image', 'category', 'peso', 'medida', 'estado']
class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ['id', 'nombre', 'estado','products']
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'email', 'password','rol', 'list']

class Clientserializer(serializers.ModelSerializer):
    class Meta:
        model = client
        fields = ['id', 'nombre', 'celular','direcciones', 'usuario', 'lists']
