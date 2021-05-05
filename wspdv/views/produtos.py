from django.shortcuts import render
from django.http import HttpResponse
from wspdv.models import Produto

def produtos(request):
    produtos = list(Produto.objects.all().values())[:]
    return render(request, 'produtos.html',{"produtos":produtos})

def adicionar_produto(request):
    descricao = request.POST["descricao"]
    preco = request.POST["preco"]
    codigo = request.POST["codigo"]
    
    produto = Produto(descricao=descricao, preco=preco, codigo=codigo)
    produto.save()
    return render(request, "produtos.html")