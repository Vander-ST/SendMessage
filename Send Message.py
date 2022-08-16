import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

contatos = ['973031263','983435229','998523733','99901-5992']      #VARIÁVEL CONTATO COMO LISTA PARA REALIZAR A PESQUISA
message = 'Mensagem de Teste do Bot.'   #MENSAGEM A SER ENVIADA
url = 'https://web.whatsapp.com/'       #PÁGINA QUE SERÁ ACESSADA
n = 1                                   #VARIÁVEL PARA UTILIZAÇÃO NO LOOPING
x = 1                                   #VARIÁVEL PARA CONTAGEM DE REPETIÇÕES

#ABRIR NAVEGADOR NA PASTA RAÍZ DO PROJETO E ATRIBUIR A VARIÁVEL DRIVER
driver = webdriver.Chrome(os.getcwd() + os.sep + 'chromedriver.exe')
#ABRIR PÁGINA ATRAVÉS DA VARIÁVEL URL ONDE SE ENCONTRA O SITE A SER ACESSADO
driver.get(url)
#ESPERAR 20 SEGUNDOS PARA O USUÁRIO CONECTAR VIA CAMERA DO CELULAR AO WHATSAPP
time.sleep(20)

#ENTRANDO NO LOOPING INFINITO POIS N SERÁ SEMPRE IGUAL A 1
while n == 1:
    for i in contatos: #LOOP PARA PERCORRER LISTA DE CONTATOS
        print(i)    #MOSTRAR CONTATO
        # ATRIBUIR E ACHAR LOCAL A CLICAR
        element = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
        element.click() #CLICAR NO LOCAL
        time.sleep(1)   #ESPERAR 1 SEGUNDO
        element.send_keys(Keys.CONTROL,'a')     #APERTAR TECLAS PARA SELECIONAR TUDO O QUE ESTIVER ESCRITO
        element.send_keys(Keys.DELETE)      #APERTAR TECLA DELETE PARA EXCLUIR O QUE ESTIVER ESCRITO
        time.sleep(1)           #ESPERAR 1 SEGUNDO
        element.send_keys(i)        #ESCREVER O NOME DO CONTATO NO LOCAL
        element.send_keys(Keys.ENTER)   #APERTAR ENTER PARA PESQUISAR
        time.sleep(1)       #ESPERAR 1 SEGUNDO
        # ATRIBUIR E ACHAR LOCAL A CLICAR
        local_mensagem = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        local_mensagem.send_keys(message)   #ESCREVER MENSAGEM ATRIBUIDA A VARIÁVEL MESSAGE
        local_mensagem.send_keys(Keys.ENTER) #APERTAR ENTER PARA ENVIAR
        time.sleep(10)      #ESPERAR 10 SEGUNDO
    print(x)        #MOSTRAR CONTAGEM
    time.sleep(30)  #ESPERAR 30 SEGUNDO
    x = x + 1       #INCREMENTAR CONTAGEM

