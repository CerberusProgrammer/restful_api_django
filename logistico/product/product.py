from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, db_column='nombre')
    description = models.TextField(db_column='descripcion')
    price = models.DecimalField(max_digits=10, decimal_places=2, db_column='precio')
    stock = models.IntegerField(db_column='disponibilidad')
    state = models.BooleanField(default=True, db_column='estado')
    creation_date = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    modification_date = models.DateTimeField(auto_now=True, db_column='fecha_modificacion')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'producto'
        indexes = [
            models.Index(fields=['name'], name='idx_name'),
            models.Index(fields=['price'], name='idx_price'),
            models.Index(fields=['state'], name='idx_state'),
            models.Index(fields=['creation_date'], name='idx_creation_date'),
            models.Index(fields=['modification_date'], name='idx_modification_date'),
        ]