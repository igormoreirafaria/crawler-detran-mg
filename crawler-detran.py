from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import codecs
driver = webdriver.Chrome(ChromeDriverManager().install())

url = 'https://www.detran.mg.gov.br/unidades/index/unidades-de-atendimento/lista-de-unidades'
driver.get(url)

tds = driver.find_elements(By.TAG_NAME, 'td')

file = codecs.open('enderecos-detran.txt', 'a',  "utf-8")

namelist = []
count = 1
while True:
    count += 1
    for i in range(60):
        tds = driver.find_elements(By.TAG_NAME, 'td')
        if (len(tds[i].find_elements(By.TAG_NAME, 'a')) > 0):
            a = tds[i].find_element(By.TAG_NAME, 'a').click()
            try:
                dd = driver.find_element(By.XPATH, '//dt[contains(text(), "Endereço:")]//following-sibling::dd')
                namelist.append(dd)
                file.write(dd.text)
                file.write('\n')
                driver.back()
            except:
                driver.back()
    
    next = driver.find_element(By.XPATH, f'//a[contains(text(), "{count}")]')
    next.click()
