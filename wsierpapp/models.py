from django.db import models
from django.contrib.auth.models import User as DjangoUser
from django.contrib.auth.hashers import make_password

class Usuario(DjangoUser):
    nome   = models.CharField(max_length=100)
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Usuario, self).save(*args, **kwargs)

    def __str__(self):
        return self.username
    
class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    nome = models.CharField(max_length=250)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
    
class ProdutoVenda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    venda = models.ForeignKey('Venda', on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    
    def __str__(self):
        return self.produto.nome
class Venda(models.Model):
    data = models.DateField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.usuario.username