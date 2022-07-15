import os
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

contatos = ['973031263','983435229','998523733','99901-5992']
message = 'Mensagem de Teste do Bot.'
url = 'https://web.whatsapp.com/'
n = 1
x = 1

driver = webdriver.Chrome(os.getcwd() + os.sep + 'chromedriver.exe')
driver.get(url)
time.sleep(20)

while n == 1:
    for i in contatos:
        print(i)
        element = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
        element.click()
        time.sleep(1)
        element.send_keys(Keys.CONTROL,'a')
        element.send_keys(Keys.DELETE)
        time.sleep(1)
        element.send_keys(i)
        element.send_keys(Keys.ENTER)
        time.sleep(1)
        local_mensagem = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        local_mensagem.send_keys(message)
        local_mensagem.send_keys(Keys.ENTER)
        time.sleep(10)
    print(x)
    time.sleep(30)
    x = x + 1

