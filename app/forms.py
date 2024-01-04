from genericpath import exists
from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError
from datetime import datetime, time
from django.contrib.auth.forms import AuthenticationForm
#formulario para registrarse


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)


#formulario para agregar productos al carrito
class AgregarAlCarritoForm(forms.Form):
    libro_id = forms.IntegerField(widget=forms.HiddenInput())
    cantidad = forms.IntegerField()

    class Meta:
        
        model = Carrito
      
        fields = ['libro_id','cantidad']

class CartaForm(ModelForm):

    codigo = forms.IntegerField(min_value=1)
    nombre = forms.CharField(min_length=3 ,max_length=20)
    descripcion = forms.CharField(min_length=3 ,max_length=300)




    class Meta:
        
        model = Carta
      
        fields = ['nombre','autor','edicion','precio', 'stock', 'imagen']




class Crearclienteform(ModelForm):
    username = forms.CharField(min_length=3, max_length=15, label="Nombre de usuario")
    password = forms.CharField(min_length=3, max_length=15, label="Contraseña")
    rut = forms.CharField(min_length=3, max_length=15, label="RUT")
    nombre = forms.CharField(min_length=3, max_length=50, label="Nombre")
    apellido = forms.CharField(min_length=3, max_length=50, label="Apellido")
    correo = forms.CharField(min_length=3, max_length=80, label="Correo electrónico")
    direccion = forms.CharField(min_length=3, max_length=80, label="Dirección")
    telefono = forms.CharField(min_length=3, max_length=20, label="Teléfono")

    class Meta:
        model = Cliente
        fields = ['username', 'password', 'rut', 'nombre', 'apellido', 'correo', 'direccion', 'telefono']

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )
        cliente = super().save(commit=False)
        cliente.user = user
        if commit:
            cliente.save()
        return cliente

class ModificarClienteForm(forms.ModelForm):
    rut = forms.CharField(min_length=3, max_length=15, label="RUT")
    nombre = forms.CharField(min_length=3, max_length=50, label="Nombre")
    apellido = forms.CharField(min_length=3, max_length=50, label="Apellido")
    correo = forms.CharField(min_length=3, max_length=80, label="Correo electrónico")
    direccion = forms.CharField(min_length=3, max_length=80, label="Dirección")
    telefono = forms.CharField(min_length=3, max_length=20, label="Teléfono")

    def save(self, commit=True):
        cliente = super().save(commit=False)
        cliente.user.first_name = self.cleaned_data['nombre']
        cliente.user.last_name = self.cleaned_data['apellido']
        cliente.user.email = self.cleaned_data['correo']
        if commit:
            cliente.save()
            cliente.user.save()
        return cliente

    class Meta:
        model = Cliente
        fields = ['rut', 'nombre', 'apellido', 'correo', 'direccion', 'telefono']

class Crearempleadoform(ModelForm):
    username = forms.CharField(min_length=3, max_length=15, label="Nombre de usuario")
    password = forms.CharField(min_length=3, max_length=15, label="Contraseña")
    rut = forms.CharField(min_length=3, max_length=15, label="RUT")
    nombre = forms.CharField(min_length=3, max_length=50, label="Nombre")
    apellido = forms.CharField(min_length=3, max_length=50, label="Apellido")
    correo = forms.CharField(min_length=3, max_length=80, label="Correo electrónico")
    direccion = forms.CharField(min_length=3, max_length=80, label="Dirección")
    telefono = forms.CharField(min_length=3, max_length=20, label="Teléfono")
    cargo = forms.CharField(min_length=3, max_length=20, label="cargo")
    departamento = forms.CharField(min_length=3, max_length=20, label="departamento")
   
    class Meta:
        model = Empleado
        fields = ['username', 'password', 'rut', 'nombre', 'apellido', 'correo', 'direccion', 'telefono','cargo','departamento']

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )
        empleado = super().save(commit=False)
        empleado.user = user
        if commit:
            empleado.save()
        return empleado

class ModificarEmpleadoForm(forms.ModelForm):
    rut = forms.CharField(min_length=3, max_length=15, label="RUT")
    nombre = forms.CharField(min_length=3, max_length=50, label="Nombre")
    apellido = forms.CharField(min_length=3, max_length=50, label="Apellido")
    correo = forms.CharField(min_length=3, max_length=80, label="Correo electrónico")
    direccion = forms.CharField(min_length=3, max_length=80, label="Dirección")
    telefono = forms.CharField(min_length=3, max_length=20, label="Teléfono")
    def save(self, commit=True):
        empleado = super().save(commit=False)
        empleado.user.first_name = self.cleaned_data['nombre']
        empleado.user.last_name = self.cleaned_data['apellido']
        empleado.user.email = self.cleaned_data['correo']
        if commit:
            empleado.save()
            empleado.user.save()
        return empleado 
    class Meta:
        model = Empleado
        fields = ['rut', 'nombre', 'apellido', 'correo', 'direccion', 'telefono']

##############################################################
#############################################################
##########################admin##############################


    
class ModificarClienteadminForm(forms.ModelForm):
    rut = forms.CharField(min_length=3, max_length=15, label="RUT")
    nombre = forms.CharField(min_length=3, max_length=50, label="Nombre")
    apellido = forms.CharField(min_length=3, max_length=50, label="Apellido")
    correo = forms.CharField(min_length=3, max_length=80, label="Correo electrónico")
    direccion = forms.CharField(min_length=3, max_length=80, label="Dirección")
    telefono = forms.CharField(min_length=3, max_length=20, label="Teléfono")

    def save(self, commit=True):
        cliente = super().save(commit=False)
        cliente.user.first_name = self.cleaned_data['nombre']
        cliente.user.last_name = self.cleaned_data['apellido']
        cliente.user.email = self.cleaned_data['correo']
        if commit:
            cliente.save()
            cliente.user.save()
        return cliente

    class Meta:
        model = Cliente
        fields = ['rut', 'nombre', 'apellido', 'correo', 'direccion', 'telefono']



class ModificarEmpleadoadminForm(forms.ModelForm):
    rut = forms.CharField(min_length=3, max_length=15, label="RUT")
    nombre = forms.CharField(min_length=3, max_length=50, label="Nombre")
    apellido = forms.CharField(min_length=3, max_length=50, label="Apellido")
    correo = forms.CharField(min_length=3, max_length=80, label="Correo electrónico")
    direccion = forms.CharField(min_length=3, max_length=80, label="Dirección")
    telefono = forms.CharField(min_length=3, max_length=20, label="Teléfono")
    cargo = forms.CharField(min_length=3, max_length=20, label="Cargo")
    departamento = forms.CharField(min_length=3, max_length=20, label="Departamento")
    def save(self, commit=True):
        empleado = super().save(commit=False)
        empleado.user.first_name = self.cleaned_data['nombre']
        empleado.user.last_name = self.cleaned_data['apellido']
        empleado.user.email = self.cleaned_data['correo']
        if commit:
            empleado.save()
            empleado.user.save()
        return empleado 
    class Meta:
        model = Empleado
        fields = ['rut', 'nombre', 'apellido', 'correo', 'direccion', 'telefono']
