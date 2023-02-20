from django.shortcuts import render
from django.db import models
import requests


# Create your views here.

def raiz(request):
    cotacao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
    cotacao = cotacao.json()
    bid = cotacao['USDBRL']['bid']
    time = cotacao['USDBRL']['create_date']
    return render(request, 'home.html', {'cotacao': bid, 'time': time})


class usuario(models.Model):
    Cod_Pro = models.CharField(max_length=20)
    Descricao = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.Cod_Pro
