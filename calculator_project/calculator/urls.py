from django.urls import path
from .views import calculator, calculate

urlpatterns = [
    path('', calculator, name='calculator'),
    path('calculate/', calculate, name='calculate'),
]

