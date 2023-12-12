from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Item

# Create your views here.
def pagina_inicial(pedido):

    if pedido.method == "POST":
        Item.objects.create(texto=pedido.POST['tarefa_texto'])
        return redirect('/')
    
    itens = Item.objects.all()

    return render(pedido, 'inicio.html', {
        'items': itens
    })