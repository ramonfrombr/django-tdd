from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
    
    def test_pode_criar_uma_lista_e_recuperar_mais_tarde(self):

        # Maria ouviu falar de um novo app de tarefas
        # Ela visita o site
        self.browser.get("http://localhost:8000")

        # Ela percebe que no título da página há a menção do nome do site
        self.assertIn("To-Do", self.browser.title)
        self.fail("Finish the test!")

        # Ela é convidada a criar um novo item na lista de tarefas imediatamente

        # Ela digita "Comprar pão" no campo

        # Quando ela aperta Enter, a página atualiza, e agora a página lista
        # "1: Comprar pão" como sendo um item da lista de tarefas

        # Ainda há um campo convidando ela a adicionar outro item.
        # Ela digita "Comprar leite"
        
        # A página atualiza novamente, e agora exibe ambos os itens na lista

        # Maria se pergunta se o site vai se lembrar da sua lista.
        # Ela vê que o site gerou um URL único para ela - o site exibe um texto explicativo dizendo isso

        # Ela visite o URL - a lista de tarefas dela ainda está lá

        # Satisfeita, ela vai dormir 


if __name__=='__main__':
    unittest.main(warnings='ignore')