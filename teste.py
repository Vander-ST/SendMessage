import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


message = 'Mensagem de Teste do Bot.'        #MENSAGEM A SER ENVIADA
url = 'https://www.google.com/'              #PÁGINA QUE SERÁ ACESSADA
n = 1                                        #VARIÁVEL PARA UTILIZAÇÃO NO LOOPING
x = 1                                        #VARIÁVEL PARA CONTAGEM DE REPETIÇÕES
contatos = ['Paçoca','Pudim','Lanche','Noite'] #VARIÁVEL CONTATO COMO LISTA PARA REALIZAR A PESQUISA

#ABRIR NAVEGADOR NA PASTA RAÍZ DO PROJETO E ATRIBUIR A VARIÁVEL DRIVER
driver = webdriver.Chrome(os.getcwd() + os.sep + 'chromedriver.exe')
#ABRIR PÁGINA ATRAVÉS DA VARIÁVEL URL ONDE SE ENCONTRA O SITE A SER ACESSADO
driver.get(url)
#ATRIBUIR A VARIÁVEL ELEMENT1 O LOCAL DA AÇÃO IDENTIFICADO
element1 = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
#CLICAR NO ELEMENTO IDENTIFICADO ACIMA
element1.click()
#ESCREVER A MENSAGEM GUARDADA NA VARIÁVEL MESSAGE
element1.send_keys(message)
#APERTAR O BOTÃO ENTER PARA ENVIAR A MENSAGEM
element1.send_keys(Keys.ENTER)


while n == 1:
    for i in contatos:
        print(i)
        element2 = driver.find_element_by_xpath('//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[2]/input')
        element2.click()
        element2.send_keys(Keys.CONTROL,'a')
        element2.send_keys(Keys.DELETE)
        element2.send_keys(i)
        element2.send_keys(Keys.ENTER)
        time.sleep(10)
    print(x)
    x = x + 1



#973031263
#983435229
#998523733