from django.db import models


class Product(models.Model):
    description = models.CharField(max_length=75, verbose_name='Descrição')
    amount = models.FloatField(verbose_name='Quantidade')
    unit = models.CharField(max_length=10, null=True, blank=True,
                            verbose_name='Unidade')
    brand = models.CharField(max_length=30, null=True, blank=True,
                             verbose_name='Marca')
    # improve with 'choices' later
    details = models.CharField(max_length=150, null=True, blank=True,
                               verbose_name='Detalhes')
    note = models.TextField(null=True, blank=True, verbose_name='Observações')

    # include picture field in the future
    # include category in the future

    def __str__(self):
        return self.description
        # TODO: testar no str um campo que não seja obrigatório

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
