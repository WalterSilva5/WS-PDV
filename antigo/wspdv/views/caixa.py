from django.shortcuts import render
from django.http import HttpResponse

def caixa(request):
    return render(request, 'caixa.html')