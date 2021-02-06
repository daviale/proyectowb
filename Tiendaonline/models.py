from django.db import models

# Create your models here.
class Rol(models.Model):
    nombre = models.CharField(max_length=20)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on= models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['created_on']
        verbose_name='rol'
        verbose_name_plural='roles'

    def __str__(self):
        return self.nombre

class Direccion(models.Model):
    nombre = models.CharField(max_length=80)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on= models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['created_on']
        verbose_name='direccion'
        verbose_name_plural='direcciones'

    def __str__(self):
        return self.nombre 
class Category(models.Model):
    nombre = models.CharField(max_length=50)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on= models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['created_on']
        verbose_name='category'
        verbose_name_plural='categorys'

    def __str__(self):
        return self.nombre

class Product (models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField("Imagen", upload_to='producctos' , blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    peso = models.IntegerField()
    medida = models.CharField(max_length=30)
    estado = models.BooleanField()
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on= models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['created_on']
        verbose_name='product'
        verbose_name_plural='products'

    def __str__(self):
        return self.nombre  

class List (models.Model):
    nombre = models.CharField(max_length=50)
    estado = models.BooleanField
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on= models.DateTimeField(auto_now=True)
 
    class Meta:
        ordering=['created_on']
        verbose_name='list'
        verbose_name_plural='lists'

    def __str__(self):
        return self.nombre   
class Usuario(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on= models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['created_on']
        verbose_name='usuario'
        verbose_name_plural='usuarios'

    def __str__(self):
        return self.email
        
class client(models.Model):
    nombre = models.CharField(max_length=50)
    celular = models.CharField(max_length=9)
    direcciones = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    usuario= models.ForeignKey(Usuario, on_delete=models.CASCADE)
    lists = models.ForeignKey(List, on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on= models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['created_on']
        verbose_name='client'
        verbose_name_plural='clients'

    def __str__(self):
        return self.nombre                      