from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from api.serializers import RolSerializer
from api.serializers import DireccionSerializer
from api.serializers import CategorySerializer
from api.serializers import ProductSerializer
from api.serializers import ListSerializer
from api.serializers import UsuarioSerializer
from api.serializers import Clientserializer


from Tiendaonline.models import Rol
from Tiendaonline.models import Direccion
from Tiendaonline.models import Category
from Tiendaonline.models import Product
from Tiendaonline.models import List
from Tiendaonline.models import Usuario
from Tiendaonline.models import client
# Create your views here.


class RolViewset(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class DireccionVIewset(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer   

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer 

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer  

class ListViewset(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer   

class UsuarioViewset(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer   

class ClientViewset(viewsets.ModelViewSet):
    queryset = client.objects.all()
    serializer_class = Clientserializer       

