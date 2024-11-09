from django.db import models

class Subasta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    precio_inicial = models.DecimalField(max_digits=10, decimal_places=2)
    precio_actual = models.DecimalField(max_digits=10, decimal_places=2)
    producto = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre