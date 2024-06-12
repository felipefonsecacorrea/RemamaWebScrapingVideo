import time

import pandas as pd
import selenium
#pip install pandas

from selenium import webdriver
from  selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#pip install selenium

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

login = 'testeremama2'
senha = 'tresletras123'
url = 'https://www.instagram.com/'
inputs = driver.find_elements(By.TAG_NAME, 'input')

driver.get(url)
time.sleep(1)
driver.find_element(By.TAG_NAME, value="input").send_keys(login)
driver.find_element(By.NAME, value="password").send_keys(senha)
botoes = driver.find_elements(By.TAG_NAME, 'button')[:]
botoes[1].click()
time.sleep(5)

url2 = 'https://www.instagram.com/remamadragaorosa/reels/'
driver.get(url2)

time.sleep(5)

# Descer a pagina
scroll_pause_time = 3  # pausa no tempo do scroll para acompanhar o processo
screen_height = driver.execute_script("return window.screen.height;")  # pega o tamanho da pagina

dados = []
idPubli = []
publicacoes = []
idvizu = 0

i = 1


while True:
    # desce a pagina no tamanho de uma tela por vez
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
    i += 1
    time.sleep(scroll_pause_time)

    link = driver.find_elements(By.CLASS_NAME, '_aajy')[:]
    print(f'Total Links: {len(link)}')

    for lk in link:
        lk.click()
        time.sleep(1.5)
        driver.back()
        time.sleep(1.5)

#        try:
#            # Aguardar até 10 segundos para o elemento estar disponível
#            vizualizacoes = WebDriverWait(lk, 1).until(
#                EC.presence_of_element_located((By.CLASS_NAME, 'html-span'))
#            ).text
#        except selenium.common.exceptions.TimeoutException:
#            vizus = '0'
#        except selenium.common.exceptions.NoSuchElementException:
#            vizus = '0'

#        dados.append(vizus)
#        idPubli.append(idvizu)

#        idvizu = idvizu + 1

#    publicacoes.append(idvizu)
#    publicacoes.extend(dados)

#    print(publicacoes)


    # atualize a altura da rolagem sempre que rolar, pois a altura da rolagem pode mudar depois que rolamos a página
    scroll_height = driver.execute_script("return document.body.scrollHeight;")
    # interrompa o loop quando a altura que precisamos rolar for maior que a altura total da rolagem
    if (screen_height) * i > scroll_height:
        break


print(f'Total rells: {len(publicacoes)}')
print(publicacoes)
