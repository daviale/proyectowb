from django.contrib import admin
from .models import Rol, Direccion, Category, Product, List, Usuario, client  
# Register your models here.
admin.site.register(Rol)
admin.site.register(Direccion)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(List)
admin.site.register(Usuario)
admin.site.register(client)