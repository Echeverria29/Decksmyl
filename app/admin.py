from django.contrib import admin
from django import forms
from .models import *

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['user','rut','nombre','apellido','correo', 'direccion','telefono','created_at','updated_at']
    search_fields = ['id']
    list_per_page = 4

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['user','rut','nombre','apellido','correo', 'direccion','telefono','cargo','departamento','created_at','updated_at']
    search_fields = ['id']
    list_per_page = 5


class CartaAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','autor','edicion','precio','stock','imagen','created_at','updated_at']
    search_fields = ['id']
    list_per_page = 6

class carritoAdmin(admin.ModelAdmin):
    list_display = ['id','carta','cantidad','imagen','created_at','updated_at']
    search_fields = ['id']
    list_per_page = 7


class ventaAdmin(admin.ModelAdmin):
    list_display = ['id','fecha_venta','cliente_id','empleado_id','created_at','updated_at']
    search_fields = ['id']
    list_per_page = 12


class pagoAdmin(admin.ModelAdmin):
    list_display = ['id','total','venta_id','created_at','updated_at']
    search_fields = ['id']
    list_per_page = 13






admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Carta, CartaAdmin)
admin.site.register(Pago, pagoAdmin)
admin.site.register(Venta, ventaAdmin)
admin.site.register(Carrito, carritoAdmin)
