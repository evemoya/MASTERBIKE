
#Rutas de Backstoness


from django.contrib import admin
from django.urls import path, include
from .views import  index, galeria, agendarhora, informaciones, tienda, regprod,cerrar_sesion, Quienes_somos, sucursal, tipos_bici, login


urlpatterns = [
    path ('', index, name='IND'),
    path ('gale/', galeria, name='GALE' ),
    path ('agenda/',agendarhora, name='AGENDARHORA'),
    path ('info/',informaciones, name='INFO'),
    path ('tienda/',tienda, name='TIENDA'),
    path ('regprod/',regprod, name='REGPROD'),
    path ('Quiene_somos/', Quienes_somos, name='QUIENESSOMOS'),
    path ('sucursal/', sucursal, name='SUCURSAL'),
    path ('tiposBici/', tipos_bici, name='TIPOBICI'),
    path ('login/', login, name= 'LOGIN'),
    path ('cerrar/', cerrar_sesion, name= 'CERRAR'),


]
