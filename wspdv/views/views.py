from django.shortcuts import render
from django.http import HttpResponse

from .vendas import vendas
from .produtos import produtos
from .clientes import clientes
from .caixa import caixa


def index(request):
    return render(request, 'index.html')







