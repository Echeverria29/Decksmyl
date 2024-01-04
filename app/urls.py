from operator import index
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
  path('login/', iniciar_sesion, name='login'),
  path('logout/', LogoutView.as_view(), name='logout'),
  path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
  path('crearclienteform/', crearclienteform, name='crearclienteform'),
  path('home/', home, name='home'),
  path('index/', index, name='index'),
  path('indexpypal/', indexpypal, name='indexpypal'),
  path('comprafinalizada/', comprafinalizada, name='comprafinalizada'),
  path('lista_cartas', lista_cartas, name='lista_cartas'),
  path('ver_carrito', ver_carrito, name='ver_carrito'),
  path('eliminar_del_carrito/<int:id>', eliminar_del_carrito, name='eliminar_del_carrito'),
  path('agregar_al_carrito',agregar_al_carrito, name='agregar_al_carrito'),
  path('listar_personas', listar_personas, name='listar_personas'),
  path('eliminarpersona/<int:id>', eliminarpersona, name='eliminarpersona'),
  path('modificliente/<int:id>', modificliente, name='modificliente'),
  path('modifiempleado/<int:id>', modifiempleado, name='modifiempleado'),
  path('realizar_compracartas/', realizar_compracartas, name='realizar_compracartas'),
  #########################################################################################
  ####################ADMIN##################################
  path('crearempleadoform/', crearempleadoform, name='crearempleadoform'),
  path('modificlienteadmin/<int:id>', modificlienteadmin, name='modificlienteadmin'),
  path('modifiempleadoadmin/<int:id>', modifiempleadoadmin, name='modifiempleadoadmin'),
  path('listar_personasadmin', listar_personasadmin, name='listar_personasadmin'),
  path('eliminarclienteadmin/<int:id>', eliminarclienteadmin, name='eliminarclienteadmin'),
  path('eliminarempleadoadmin/<int:id>', eliminarempleadoadmin, name='eliminarempleadoadmin'),
  

]   

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)