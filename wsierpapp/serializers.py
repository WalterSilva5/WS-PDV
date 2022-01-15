from rest_framework import serializers
from wsierpapp.models import (
    Usuario, Categoria, Produto, ProdutoVenda, Venda)


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'username', 'password', 'nome')


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nome')


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ('id', 'nome', 'preco', 'categoria')
    

class ProdutoVendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdutoVenda
        fields = ('id', 'produto', 'venda', 'quantidade')


class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = ('id', 'data', 'usuario')
        