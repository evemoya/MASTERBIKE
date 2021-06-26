from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(primary_key=True,max_length=40)

    def __str__(self) -> str:
        return self.nombre

class Producto(models.Model):
    id_auto_inc = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.IntegerField()
    foto = models.ImageField(upload_to='media/productos', null=True)
    publicado = models.BooleanField(default=False)
    portada = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return "Numero:"+str(self.id_auto_inc)

 