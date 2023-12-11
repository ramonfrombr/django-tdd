from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pagina_inicial(pedido):
    return HttpResponse('<html><title>Listas de Tarefas</title></html>')