from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

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
        self.assertIn("Listas de Tarefas", self.browser.title)
        
        texto_cabecalho = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("Tarefas", texto_cabecalho)

        # Ela é convidada a criar um novo item na lista de tarefas imediatamente
        input_nova_tarefa = self.browser.find_element(By.ID, "id_nova_tarefa")

        self.assertEqual(input_nova_tarefa.get_attribute("placeholder"), "Escreva uma nova tarefa")

        # Ela digita "Comprar pão" no campo
        input_nova_tarefa.send_keys("Comprar pão")

        # Quando ela aperta Enter, a página atualiza, e agora a página lista
        # "1: Comprar pão" como sendo um item da lista de tarefas
        input_nova_tarefa.send_keys(Keys.ENTER)
        time.sleep(1)

        tabela = self.browser.find_element(By.ID, "id_tabela_lista")

        linhas = tabela.find_elements(By.TAG_NAME, 'tr')

        self.assertIn("1: Comprar pão", [linha.text for linha in linhas])


        input_nova_tarefa = self.browser.find_element(By.ID, "id_nova_tarefa")

        input_nova_tarefa.send_keys("Comprar leite")

        input_nova_tarefa.send_keys(Keys.ENTER)

        time.sleep(1)

        tabela = self.browser.find_element(By.ID, "id_tabela_lista")

        linhas = tabela.find_elements(By.TAG_NAME, 'tr')

        self.assertIn("1: Comprar pão", [linha.text for linha in linhas])
        self.assertIn("2: Comprar leite", [linha.text for linha in linhas])


        # Ainda há um campo convidando ela a adicionar outro item.
        # Ela digita "Comprar leite"
        self.fail("Termine o teste")

        # A página atualiza novamente, e agora exibe ambos os itens na lista

        # Maria se pergunta se o site vai se lembrar da sua lista.
        # Ela vê que o site gerou um URL único para ela - o site exibe um texto explicativo dizendo isso

        # Ela visite o URL - a lista de tarefas dela ainda está lá

        # Satisfeita, ela vai dormir 


if __name__=='__main__':
    unittest.main(warnings='ignore')