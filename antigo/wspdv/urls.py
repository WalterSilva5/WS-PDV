from wspdv.views.produtos import adicionar_produto
from django.urls import path
#views
from wspdv.views.views import *
urlpatterns = [
   path('', index, name='index'),
   path('vendas', vendas, name='vendas'),
   #produtos
   path('produtos', produtos, name='produtos'),
   path('produtos/adicionar_produto', adicionar_produto, name="adicionar_produto"),
   path('clientes', clientes, name='clientes'),
   path('caixa', caixa, name='caixa'),
]
