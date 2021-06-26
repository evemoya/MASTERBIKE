from django.db.models.fields.related import ForeignObject
from django.shortcuts import render
from .models import Categoria, Producto

#IMPORTAR LIBRERIA PARA AUTENTICAR :  LOGIN
from django.contrib.auth import authenticate, logout, login as login_aut
#IMPORTAR LIBRERIA DECORADORA EVITA INGRESO A PAGINAS SIN AUTORIZACION
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    tipos =  ["asesoria Corte pelo", "Asesoria corte Barba", "Asesoria tratamientos faciales" ]
    productos = Producto.objects.filter(portada=True)
    contexto = {"tipos":tipos, "productos":productos}
    return render(request, "index.html", contexto)

def galeria(request):
    return render(request, "galeria.html")

@login_required(login_url='/login/')
def agendarhora(request):
    return render(request, "agendarhora.html")

def informaciones(request):
    return render(request, "informaciones.html")

def tienda(request):
    productos = Producto.objects.filter(publicado=True)
    contexto = {"productos" : productos}
    return render(request, "tienda.html", contexto)

def Quienes_somos(request):
    return render(request, "Quienes_somos.html")

def sucursal(request):
    return render(request, "sucursal.html")

def tipos_bici(request):
    return render(request, "tipos_bici.html")

def login(request):
    mensaje= ""
    if request.POST:
        nombre = request.POST.get("txtUsuario")
        contra = request.POST.get("txtPass")
        us = authenticate(request,username=nombre, password=contra)
        if us is not None and us.is_active:
            login_aut(request,us)
            categoria = Categoria.objects.all()
            productos = Producto.objects.filter(portada=True)
            mensaje = "usuario logueado"
            contexto = {"productos":productos,"mensaje":mensaje , "categoria": categoria}
            return render(request, "index.html", contexto)
        else:
            mensaje = "usuario o contrasena incorrecto"
    contexto = {"mensaje":mensaje}
    return render(request, "login.html", contexto)

def cerrar_sesion(request):
    logout(request)
    productos = Producto.objects.filter(portada=True)
    contexto = {"productos":productos}
    return render(request, "index.html", contexto)

##############################
##############################


def regprod(request):
    categorias = Categoria.objects.all()
    contexto = {"categorias" : categorias}

    if request.POST:
        nombre = request.POST.get("txtNombre")
        precio = request.POST.get("txtPrecio")
        desc = request.POST.get("txtDesc")
        foto = request.FILES.get("txtImg")
        cate = "productos"
        obj_categoria = Categoria.objects.get(nombre=cate)

        prod = Producto(
            nombre=nombre,
            precio=precio,
            descripcion=desc,
            foto = foto,
            categoria = obj_categoria
            )
        prod.save()
        contexto = {"categorias" : categorias, "mensaje":"producto grabado"}
    return render(request, "regprod.html", contexto)



#def registrarCuenta(reques) / Metodo Pendiente
#def regHora(reques) / Metodo Pendiente



    ##############################

class persona:
    def __init__ (self, nombre,edad):
        self.nombre=nombre
        self.edad=edad
        super().__init__()
