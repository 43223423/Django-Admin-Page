

from django.shortcuts import render
from django.db import models
from django.contrib import admin
import requests
from django.apps import apps
from django.contrib import admin
from .models import usuario

from django.apps import apps

# Create your views here.

def raiz(request):
     cotacao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
     cotacao = cotacao.json()
     bid = cotacao['USDBRL']['bid']
     time = cotacao['USDBRL']['create_date']
     return render(request, 'home.html', {'cotacao': bid, 'time': time})


def resposta(request):

    descri = request.GET['descricao']
    codigo = request.GET['produto']

    Answer = usuario(
        Descricao=descri ,
        Cod_Pro= codigo

    )
    Answer.save()
    # url = 'http://127.0.0.1:8000/myapp/?descricao=thiago&produto=12345'
    return render(request, 'home.html')

def tabela(request):
    return render(request, 'tabela.html')





# class answer(request.admin.ModelAdmin):
#     descri = request.GET['descricao']
#     codigo = request.GET['produto']
#     Nome_Produto = codigo.models.CharField(max_length=20)
#     Des_Produto = descri.models.CharField(max_lenght=20)
#     admin.site.register(codigo, descri)

# class usuario(models.Model):
#     Cod_Pro = models.CharField(max_length=20)
#     Descricao = models.CharField(max_length=50)
#
#     def __str__(self) -> str:
#         return self.Cod_Pro
#

class recentes(admin.ModelAdmin):
    list_per_page = {'Cod_Prod'}
