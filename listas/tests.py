from django.test import TestCase
from django.urls import resolve
from listas.views import pagina_inicial
from django.http import HttpRequest
from django.template.loader import render_to_string

class TestePaginaInicial(TestCase):
    def test_usa_template_inicio(self):
        resposta = self.client.get('/')
        self.assertTemplateUsed(resposta, 'inicio.html')
    
    def test_pode_salvar_um_pedido_POST(self):
        resposta = self.client.post('/', data={'tarefa_texto': "Um novo item"})
        self.assertIn("Um novo item", resposta.content.decode())
        self.assertTemplateUsed(resposta, 'inicio.html')