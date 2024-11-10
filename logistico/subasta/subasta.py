from django.db import models

class Subasta(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()
    state = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField('product.Product', related_name='subastas')
    modification_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name