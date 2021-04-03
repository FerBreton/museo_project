from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('entrada', Entrada.as_view(), name='entrada'),
]