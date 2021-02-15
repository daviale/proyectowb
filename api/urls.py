from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register(r'roles', views.RolViewset )
router.register(r'direcciones', views.DireccionVIewset )
router.register(r'categorias', views.CategoryViewset )
router.register(r'productos', views.ProductViewset )
router.register(r'Listas', views.ListViewset )
router.register(r'Usuarios', views.UsuarioViewset)
router.register(r'Clientes', views.ClientViewset )



urlpatterns = [
    path(r'', include(router.urls)),
    

    

]