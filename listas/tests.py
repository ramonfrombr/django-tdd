from django.test import TestCase
from django.urls import resolve
from listas.views import pagina_inicial

class TesteQualquer(TestCase):
    def test_url_raiz_redireciona_para_pagina_inicial(self):
        funcao_encontrada = resolve('/')
        self.assertEqual(funcao_encontrada.func, pagina_inicial)