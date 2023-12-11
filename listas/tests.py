from django.test import TestCase

class TesteQualquer(TestCase):
    def test_matematica_ruim(self):
        self.assertEqual(1+1, 3)