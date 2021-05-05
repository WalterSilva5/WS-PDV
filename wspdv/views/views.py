from django.shortcuts import render
from django.http import HttpResponse

from .vendas import *
from .produtos import *
from .clientes import *
from .caixa import *


def index(request):
    return render(request, 'index.html')







