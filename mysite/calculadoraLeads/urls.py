from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculadora, name='calculadora'),
    path('ltv/', views.ltv, name='ltv'),
    path('valor/', views.valor, name='valor'),
]