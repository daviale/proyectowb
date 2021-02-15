from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

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
    path(r'auth/login', obtain_jwt_token),
    path(r'auth/refresh-token', refresh_jwt_token),
    path(r'auth/verify-token', verify_jwt_token),

    

]