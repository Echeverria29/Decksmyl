
from django.shortcuts import render,redirect,get_object_or_404
import requests
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import ValidationError
from datetime import date
from django.db import transaction
from django.contrib.auth import logout
from django.contrib.auth.models import User
#AL COMPRAR TE MUESTRA ESTA PAGINA PARA IR A TU SEGUIMIENTO

def comprafinalizada(request):
    return render(request,'app/comprafinalizada.html')

#PAGINA PARA MOSTRAR TUS DATOS DE USUARIO
@login_required
def home(request):
  return render(request,'app/home.html')

def index(request):
  return render(request,'app/index.html')

#PAGINA PARA REALIZAR EL PAGO SIMULADO CON EL SCRIPT
@login_required
def indexpypal(request):
  return render(request,'app/indexpypal.html')


#INICIO SE SESION
def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

#CERRAR SESION
@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('index')

#FORMULARIO PARA CREAR AL CLIENTE
def crearclienteform(request):
    if request.method == 'POST':
        form = Crearclienteform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente registrado correctamente')
    else:
        form = Crearclienteform()
    return render(request, 'app/crearclienteform.html', {'form': form})

#FORMULARIO PARA CREAR AL EMPLEADO
@login_required
def crearempleadoform(request):
    if request.method == 'POST':
        form = Crearempleadoform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empleado registrado correctamente')
    else:
        form = Crearempleadoform()
    return render(request, 'app/crearempleadoform.html', {'form': form})



#FORMULARIO PARA MODIFICAR DATOS CLIENTE
@login_required
def modificliente (request, id):
    cliente = Cliente.objects.get(user_id=id)
    datos = {
        'form' : ModificarClienteForm(instance=cliente)
    }
    if request.method == 'POST':
        formulario = ModificarClienteForm(data=request.POST, files=request.FILES, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, '¡Modificación de datos exitosa!')
            datos['form'] = formulario

    return render(request, 'app/modificliente.html', datos)

@login_required
def modifiempleado (request, id):
    empleado = Empleado.objects.get(user_id=id)
    datos = {
        'form' : ModificarEmpleadoForm(instance=empleado)
    }
    if request.method == 'POST':
        formulario = ModificarEmpleadoForm(data=request.POST, files=request.FILES, instance=empleado)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, '¡Modificación de datos exitosa!')
            datos['form'] = formulario

    return render(request, 'app/modifiempleado.html', datos)



#funcion para listar los libros agregados
@login_required
def lista_cartas(request):
    cartas = Carta.objects.all()
    form = AgregarAlCarritoForm()
    return render(request, 'app/lista_libros.html', {'cartas': cartas, 'form': form})




#funcion para agregar un libro al carrito y sumar las cantidades ingresadas con el id del libro
@login_required
def agregar_al_carrito(request):
    if request.method == 'POST':
        carta_id = request.POST.get('carta_id')
        cantidad = int(request.POST.get('cantidad', 1))
        carta = get_object_or_404(Carta, id=carta_id)
        carrito = Carrito.objects.filter(usuario=request.user, carta=carta).first()
        if carrito:
            carrito.cantidad += cantidad
            carrito.save()
            messages.success(request, f'Se han agregado {cantidad} "{libro.nombre}" al carrito.')
        else:
            carrito = Carrito.objects.create(usuario=request.user, libro=libro, cantidad=cantidad)
            messages.success(request, f'Se ha agregado "{libro.nombre}" al carrito.')

        carrito.imagen = libro.imagen
        carrito.save()
    return redirect('../lista_libros')


#funcion para ver los libros agregados al carrito
@login_required
def ver_carrito(request):
    carrito = Carrito.objects.filter(usuario=request.user)
    total = sum(item.subtotal() for item in carrito)
    context = {
        'carrito': carrito,
        'total': total
    }
    return render(request, 'app/ver_carrito.html', context)


#funcion para eliminar el lo que esta en el carrito
@login_required
def eliminar_del_carrito(request, id):
    carrito = get_object_or_404(Carrito, id=id,usuario=request.user)
    if request.method == 'POST':
        carrito.delete()
       
    return redirect('ver_carrito')

#FUNCION PARA LISTAR LOS DATOS DEL CLIENTE LA PAGINA PRINCIPAL
@login_required
def listar_personas(request):
    cliente = Cliente.objects.all()
    
     
    datos = {
        #como dato estas listas van en las paginas listar_...
        
        'listaClientes': cliente,
        
        
    }
    return render(request, 'app/listar_personas.html', datos)




#FUNCION PARA ELIMINAR LOS CLIENTES DEL EMPLEADO
@login_required
def eliminarpersona(request, id):
    cliente = Cliente.objects.get(id=id)
    user = cliente.user

    # Eliminar el cliente y el usuario
    cliente.delete()
    user.delete()

    

    return redirect('listar_personas')

#FUNCION PARA POBLAR LAS TABLAS VENTA Y PAGO AL MISMO TIEMPO
@login_required
def realizar_compracartas(request):
    carrito = Carrito.objects.all()  # Obtener el  objetos del modelo Carrito del usuario actual
    cliente = Cliente.objects.filter(user=request.user).first()  # Obtener el objeto Cliente del usuario actual
    
    # Iterar sobre cada objeto en el carrito
    for item in carrito:
        carta = item.carta  # Obtener el libro del carrito
    
        if request.method == 'POST':

            total = sum(item.subtotal() for item in carrito)

            # Obtener el cliente y empleado de la base de datos
            cliente = Cliente.objects.first()
            empleado = Empleado.objects.first()

            with transaction.atomic():
                # Crear una nueva venta
                venta = Venta(
                    fecha_venta=date.today(),
                    total=total,
                    cliente=cliente,
                    empleado=empleado
                )
                venta.save()

                # Obtener el objeto Venta recién creado
                venta = Venta.objects.latest('id')

                # Crear un nuevo pago relacionado con la venta
                pago = Pago(
                    total=total,
                    venta=venta
                )
                pago.save()
                carta.stock -= item.cantidad  # Actualizar el stock del libro
                carta.save()  # Guardar los cambios en el libro
        
       
    return redirect('indexpypal')  # Redirigir al usuario a la lista de libros después de realizar las compras


###############################################################################
############################################################################
#################SECCION DE CRUD DEL ADMIN####################################
@login_required
def modificlienteadmin (request, id):
    cliente = Cliente.objects.get(id=id)
    datos = {
        'form' : ModificarClienteadminForm(instance=cliente)
    }
    if request.method == 'POST':
        formulario = ModificarClienteadminForm(data=request.POST, files=request.FILES, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, '¡Modificación de datos exitosa!')
            datos['form'] = formulario

    return render(request, 'app/modificlienteadmin.html', datos)

@login_required
def modifiempleadoadmin (request, id):
    empleado = Empleado.objects.get(id=id)
    datos = {
        'form' : ModificarEmpleadoadminForm(instance=empleado)
    }
    if request.method == 'POST':
        formulario = ModificarEmpleadoadminForm(data=request.POST, files=request.FILES, instance=empleado)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, '¡Modificación de datos exitosa!')
            datos['form'] = formulario

    return render(request, 'app/modifiempleadoadmin.html', datos)

@login_required
def listar_personasadmin(request):
    cliente = Cliente.objects.all()
    empleado = Empleado.objects.all()
    
     
    datos = {
        #como dato estas listas van en las paginas listar_...
        
        'listaClientes': cliente,
        'listaEmpleados': empleado
        
        
    }
    return render(request, 'app/listar_personasadmin.html', datos)

@login_required
def eliminarclienteadmin(request, id):
    cliente = Cliente.objects.get(id=id)
    user = cliente.user

    # Eliminar el cliente y el usuario
    cliente.delete()
    user.delete()

   

    return redirect('listar_personasadmin')

@login_required
def eliminarempleadoadmin(request, id):
    empleado = Empleado.objects.get(id=id)
    user = empleado.user

    # Eliminar el empleado y el usuario
    empleado.delete()
    user.delete()

    

    return redirect('listar_personasadmin')

