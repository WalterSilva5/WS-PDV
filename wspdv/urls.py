from django.urls import path
#views
from wspdv.views import index, vendas, produtos, clientes, caixa
urlpatterns = [
   path('', index, name='index'),
   path('vendas', vendas, name='vendas'),
   path('produtos', produtos, name='produtos'),
   path('clientes', clientes, name='clientes'),
   path('caixa', caixa, name='caixa'),
]
