from django.db import models

# Create your models here.

class Produto(models.Model):
    codigo = models.IntegerField(unique=True, blank=False)
    descricao = models.CharField(max_length=200, blank=False)
    preco = models.DecimalField(max_digits=19, decimal_places=10, blank=False)

    class Meta:
    	verbose_name = 'Produto'
    	verbose_name_plural = 'Produtos'
    
    def __str__():
    	return self.descricao