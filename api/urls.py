from api.views import ProdutoViewSet
from django.conf.urls import include
from django.urls.conf import path
from rest_framework import routers

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = routers.DefaultRouter()
router.register(r'produtos', ProdutoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('api/token/', TokenObtainPairView.as_view()),
    # path('api/token/refresh', TokenRefreshView.as_view())
]
