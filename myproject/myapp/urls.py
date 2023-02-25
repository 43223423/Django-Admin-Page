from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.raiz, name='raiz'),
    # path('', views.tabela, name='table'),
    path('resposta', views.resposta, name='resposta'),
    path('tabela/', views.tabela, name='tabela')
]
