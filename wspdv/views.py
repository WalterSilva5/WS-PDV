from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def vendas(request):
    return render(request, 'vendas.html')

def produtos(request):
    return render(request, 'produtos.html')

def clientes(request):
    return render(request, 'clientes.html')

def caixa(request):
    return render(request, 'caixa.html')


