from django.test import TestCase
from django.urls import resolve
from listas.views import pagina_inicial
from django.http import HttpRequest
from django.template.loader import render_to_string
from listas.models import Item

class TestePaginaInicial(TestCase):
    def test_usa_template_inicio(self):
        resposta = self.client.get('/')
        self.assertTemplateUsed(resposta, 'inicio.html')
    
    def test_pode_salvar_um_pedido_POST(self):
        resposta = self.client.post('/', data={'tarefa_texto': "Um novo item"})
        self.assertIn("Um novo item", resposta.content.decode())
        self.assertTemplateUsed(resposta, 'inicio.html')

    def test_salvar_e_selecionar_itens(self):
        primeiro_item = Item()
        primeiro_item.texto = "Primeiro item"
        primeiro_item.save()

        segundo_item = Item()
        segundo_item.texto = "Segundo item"
        segundo_item.save()

        itens_salvos = Item.objects.all()
        self.assertEqual(itens_salvos.count(), 2)

        primeiro_item_salvo = itens_salvos[0]
        segundo_item_salvo = itens_salvos[1]
        self.assertEqual(primeiro_item_salvo.texto, "Primeiro item")
        self.assertEqual(segundo_item_salvo.texto, "Segundo item")