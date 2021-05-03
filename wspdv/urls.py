from django.urls import path
#views
from wspdv.views import index
urlpatterns = [
   path('', index, name='index'),
]
