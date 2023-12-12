from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pagina_inicial(pedido):
    return render(pedido, 'inicio.html', {
        'nova_tarefa_texto': pedido.POST.get('tarefa_texto', '')
    })