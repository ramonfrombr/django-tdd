from django.test import TestCase
from django.urls import resolve
from listas.views import pagina_inicial
from django.http import HttpRequest
from django.template.loader import render_to_string

class TestePaginaInicial(TestCase):
    def test_usa_template_inicio(self):
        resposta = self.client.get('/')
        self.assertTemplateUsed(resposta, 'inicio.html')