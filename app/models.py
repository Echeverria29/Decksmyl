
from django.db import models
from django.contrib.auth.models import User
from unittest.util import _MAX_LENGTH

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True

    

    def actualizar_user_fields(self):
        
        self.user.first_name = self.nombre
        self.user.last_name = self.apellido
        self.user.email = self.correo
        self.user.save()

class Empleado(Perfil):
    cargo = models.CharField(max_length=50)
    departamento = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        created = not bool(self.pk)
        super().save(*args, **kwargs)
        if created:
            self.actualizar_user_fields()

class Cliente(Perfil):
  

    def save(self, *args, **kwargs):
        created = not bool(self.pk)
        super().save(*args, **kwargs)
        if created:
            self.actualizar_user_fields()


class Venta(models.Model):
   
    fecha_venta = models.DateField()
    total = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        
        db_table = 'venta'

class Pago(models.Model):
   
    total = models.IntegerField()
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.total
    class Meta:
       
        db_table = 'pago'


class Carta(models.Model):
   
    nombre = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    edicion = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to="Carta", null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def stockfinal(self):
      return self.stock - self.carrito.cantidad

    def __str__(self):
      return self.nombre
  

    class Meta:
       
        db_table = 'carta'

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    carta = models.ForeignKey(Carta, models.CASCADE)
    cantidad = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to="Carrito", null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def subtotal(self):
        return self.libro.precio * self.cantidad

    def __str__(self):
        return self.libro.nombre
    
    class Meta:
        
        db_table = 'carrito'

class DetalleVenta(models.Model):
    
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)  
    carta = models.ForeignKey(Carta, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        
        db_table = 'detalle_venta'
      



