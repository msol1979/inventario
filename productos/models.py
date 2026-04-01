from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    class Meta:
        db_table = 'productos'  # usa la tabla que ya existe en MySQL

    def __str__(self):
        return self.nombre
