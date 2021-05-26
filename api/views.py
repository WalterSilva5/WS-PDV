from rest_framework import generics, response
from rest_framework.generics import get_object_or_404
from api.serializers import ProdutoSerializer
from api.models import Produto
from rest_framework import viewsets
from rest_framework import status


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
