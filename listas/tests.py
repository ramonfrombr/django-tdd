from django.test import TestCase
from django.urls import resolve
from listas.views import pagina_inicial
from django.http import HttpRequest

class TestePaginaInicial(TestCase):
    def test_url_raiz_redireciona_para_pagina_inicial(self):
        funcao_encontrada = resolve('/')
        self.assertEqual(funcao_encontrada.func, pagina_inicial)

    def test_pagina_inicial_retorna_html_correto(self):
        pedido = HttpRequest()
        resposta = pagina_inicial(pedido)
        html = resposta.content.decode('utf8')

        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Lista de Tarefas', html)
        self.assertTrue(html.strip().endswith('</html>'))