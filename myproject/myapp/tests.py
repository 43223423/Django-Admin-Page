from django.test import TestCase
from django.shortcuts import render
# Create your tests here.
import requests
from django.apps import apps
from django.contrib import admin


# def resposta(request, admin):
#     url = 'http://127.0.0.1:8000/myapp/?descricao=thiago&produto=12345'
#     descri = request.GET['descricao']
#     codigo = request.GET['produto']
#     print(descri)
#     print(codigo)
#
#
#     #admin.site.register(codigo,descri)
