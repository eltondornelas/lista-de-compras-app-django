from django.db import models
from product.models import Product
from django.contrib.auth.models import User


class Lista(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    name_lista = models.CharField(max_length=30, verbose_name='Nome da Lista')
    produtos = models.ManyToManyField(Product,
                                      verbose_name='Produtos', null=True,
                                      blank=True)

    def __str__(self):
        return self.name_lista

    class Meta:
        verbose_name = 'Lista de Compras'
        verbose_name_plural = 'Lista de Compras'
