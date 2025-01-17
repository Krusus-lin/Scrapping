from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time

np.seterr(all='ignore')

#Set Selenium

service = Service("scrappingfolder/chromedriver.exe")
driver = webdriver.Chrome(service=service)

#Headers
nom=[]
format=[]
price=[]
price2 = []
url=[]

"""
#Karite
for pag in range(1,2):
    URL = 'https://www.karitelaserena.cl/catalogo/aromas?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'col-lg-4 col-6 px-md-2 px-1'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'brand-name small trsn'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'list-price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://www.karitelaserena.cl/mantecas?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'col-lg-4 col-6 px-md-2 px-1'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'brand-name small trsn'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'list-price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,3):
    URL = 'https://www.karitelaserena.cl/aceites-esenciales-katmandu?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'col-lg-4 col-6 px-md-2 px-1'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'brand-name small trsn'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'list-price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://www.karitelaserena.cl/colorantes-y-polvos?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'col-lg-4 col-6 px-md-2 px-1'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'brand-name small trsn'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'list-price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://www.karitelaserena.cl/emulsionantes-y-ceras?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'col-lg-4 col-6 px-md-2 px-1'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'brand-name small trsn'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'list-price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://www.karitelaserena.cl/activos?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'col-lg-4 col-6 px-md-2 px-1'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'brand-name small trsn'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'list-price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://www.karitelaserena.cl/bases?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'col-lg-4 col-6 px-md-2 px-1'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'brand-name small trsn'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'list-price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://www.karitelaserena.cl/hierba?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'col-lg-4 col-6 px-md-2 px-1'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'brand-name small trsn'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'list-price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://www.karitelaserena.cl/preservante?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'col-lg-4 col-6 px-md-2 px-1'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'brand-name small trsn'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'list-price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://www.karitelaserena.cl/tensioactivos?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'col-lg-4 col-6 px-md-2 px-1'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'brand-name small trsn'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'list-price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://www.karitelaserena.cl/otros?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'col-lg-4 col-6 px-md-2 px-1'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'brand-name small trsn'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'list-price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://www.karitelaserena.cl/accesorios?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'col-lg-4 col-6 px-md-2 px-1'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'brand-name small trsn'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'list-price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,3):
    URL = 'https://www.karitelaserena.cl/para-jabones?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'col-lg-4 col-6 px-md-2 px-1'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'brand-name small trsn'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'list-price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,3):
    URL = 'https://www.karitelaserena.cl/envases?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'col-lg-4 col-6 px-md-2 px-1'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'brand-name small trsn'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'list-price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://www.karitelaserena.cl/tapas?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'col-lg-4 col-6 px-md-2 px-1'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'brand-name small trsn'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'list-price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://www.karitelaserena.cl/productos-cosmeticos?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'col-lg-4 col-6 px-md-2 px-1'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'brand-name small trsn'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'list-price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://www.karitelaserena.cl/hazla-tu-misma?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'col-lg-4 col-6 px-md-2 px-1'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'brand-name small trsn'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'list-price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

df = pd.DataFrame({'Producto':nom, 'Precio':price, 'URL':url})
df.to_csv('karite.csv', index=False, encoding='utf-8')
"""
"""
#Reachem
def scrape_reachem(url, category_name):
    print(f"Scraping categoría: {category_name}")
    driver.get(url)
    time.sleep(4)

    scroll_pause_time = 2
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    prods = soup.find_all('div', {'class': 'product-wrapper'})

    nom, price, price2, url_list = [], [], [], []
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class': 'product-element-bottom'})
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text.strip()
        nom.append(nomProdname)
        url_list.append(nomProdtext['href'])

        nomProdPrice = itemProd.find('span', {'class': 'price'})
        if nomProdPrice:
            priceNum = nomProdPrice.text.replace('.', '').replace('$', '').replace(' ', '')
            priceNum = priceNum.split('–')

            if len(priceNum) == 1:
                price.append(re.findall("\d+", priceNum[0])[0])
                price2.append('')
            else:
                price.append(re.findall("\d+", priceNum[0])[0])
                price2.append(re.findall("\d+", priceNum[1])[0])
        else:
            price.append('')
            price2.append('')

    
    df = pd.DataFrame({'Producto': nom, 'PrecioMín': price, 'PrecioMáx': price2, 'URL': url_list})
    df['Categoría'] = category_name
    return df

#Lista de URLs y nombres de categorías
categories = {
    'https://reachem.cl/categoria-producto/envases/': 'Envases',
    'https://reachem.cl/categoria-producto/perfumeria/': 'Perfumería',
    'https://reachem.cl/categoria-producto/materias-primas/': 'Materias Primas',
    'https://reachem.cl/categoria-producto/higieneysalud/': 'Higiene y Salud',
    'https://reachem.cl/categoria-producto/productos-quimicos/matelabeinstru/': 'Lab e instrumentos',
    'https://reachem.cl/categoria-producto/matcolegio/': 'Materiales colegio',
}

#Dataframe final
final_df = pd.DataFrame()

#Recorrer todas las categorías
for url, category_name in categories.items():
    category_df = scrape_reachem(url, category_name)
    final_df = pd.concat([final_df, category_df], ignore_index=True)

#Guardar datos en .CSV
final_df.to_csv('reachem_all_categories.csv', index=False, encoding='utf-8')

#Cerrar el driver
driver.quit()
"""
"""
#Spacionatural
for pag in range(1,3):
    URL = 'https://spacionatural.cl/collections/aceites-esenciales/?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('product-card', {'class':'product-card'})
    #print(prods)
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-card__info empty:hidden'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('price-list',{'class':'price-list'})
        priceNum = nomProdPrice.text
        #print(priceNum)
        priceNum = priceNum.replace('.','')
        
        priceNum = priceNum.split('$') #--> ['\nPrecio de oferta', '19800\nPrecio normal', '22000']
        
        if len(priceNum) == 2:
            priceNum = priceNum[1]
        elif len(priceNum) == 3:
            priceNum = priceNum[2]

        priceNum = priceNum.replace(' ','')
        #print(priceNum)
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

#print("Len nom", len(nom))
#print("Len format", len(format))
#print("Len price", len(price))
#print("Len url", len(url))

for pag in range(1,2):
    URL = 'https://spacionatural.cl/collections/aceites-vegetales/?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('product-card', {'class':'product-card'})
    #print(prods)
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-card__info empty:hidden'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('price-list',{'class':'price-list'})
        priceNum = nomProdPrice.text
        #print(priceNum)
        priceNum = priceNum.replace('.','')
        
        priceNum = priceNum.split('$') #--> ['\nPrecio de oferta', '19800\nPrecio normal', '22000']
        
        if len(priceNum) == 2:
            priceNum = priceNum[1]
        elif len(priceNum) == 3:
            priceNum = priceNum[2]

        priceNum = priceNum.replace(' ','')
        #print(priceNum)
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://spacionatural.cl/collections/efervecentes-sales-y-otros/?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('product-card', {'class':'product-card'})
    #print(prods)
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-card__info empty:hidden'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('price-list',{'class':'price-list'})
        priceNum = nomProdPrice.text
        #print(priceNum)
        priceNum = priceNum.replace('.','')
        
        priceNum = priceNum.split('$') #--> ['\nPrecio de oferta', '19800\nPrecio normal', '22000']
        
        if len(priceNum) == 2:
            priceNum = priceNum[1]
        elif len(priceNum) == 3:
            priceNum = priceNum[2]

        priceNum = priceNum.replace(' ','')
        #print(priceNum)
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])


for pag in range(1,2):
    URL = 'https://spacionatural.cl/collections/activos-y-aditivos-cosmeticos/?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('product-card', {'class':'product-card'})
    #print(prods)
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-card__info empty:hidden'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('price-list',{'class':'price-list'})
        priceNum = nomProdPrice.text
        #print(priceNum)
        priceNum = priceNum.replace('.','')
        
        priceNum = priceNum.split('$') #--> ['\nPrecio de oferta', '19800\nPrecio normal', '22000']
        
        if len(priceNum) == 2:
            priceNum = priceNum[1]
        elif len(priceNum) == 3:
            priceNum = priceNum[2]

        priceNum = priceNum.replace(' ','')
        #print(priceNum)
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://spacionatural.cl/collections/glicerina-para-hacer-jabones/?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('product-card', {'class':'product-card'})
    #print(prods)
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-card__info empty:hidden'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('price-list',{'class':'price-list'})
        priceNum = nomProdPrice.text
        #print(priceNum)
        priceNum = priceNum.replace('.','')
        
        priceNum = priceNum.split('$') #--> ['\nPrecio de oferta', '19800\nPrecio normal', '22000']
        
        if len(priceNum) == 2:
            priceNum = priceNum[1]
        elif len(priceNum) == 3:
            priceNum = priceNum[2]

        priceNum = priceNum.replace(' ','')
        #print(priceNum)
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://spacionatural.cl/collections/bases-para-cremas/?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('product-card', {'class':'product-card'})
    #print(prods)
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-card__info empty:hidden'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('price-list',{'class':'price-list'})
        priceNum = nomProdPrice.text
        #print(priceNum)
        priceNum = priceNum.replace('.','')
        
        priceNum = priceNum.split('$') #--> ['\nPrecio de oferta', '19800\nPrecio normal', '22000']
        
        if len(priceNum) == 2:
            priceNum = priceNum[1]
        elif len(priceNum) == 3:
            priceNum = priceNum[2]

        priceNum = priceNum.replace(' ','')
        #print(priceNum)
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])
            
for pag in range(1,2):
    URL = 'https://spacionatural.cl/collections/bases-para-shampoo/?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('product-card', {'class':'product-card'})
    #print(prods)
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-card__info empty:hidden'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('price-list',{'class':'price-list'})
        priceNum = nomProdPrice.text
        #print(priceNum)
        priceNum = priceNum.replace('.','')
        
        priceNum = priceNum.split('$') #--> ['\nPrecio de oferta', '19800\nPrecio normal', '22000']
        
        if len(priceNum) == 2:
            priceNum = priceNum[1]
        elif len(priceNum) == 3:
            priceNum = priceNum[2]

        priceNum = priceNum.replace(' ','')
        #print(priceNum)
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://spacionatural.cl/collections/ceras/?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('product-card', {'class':'product-card'})
    #print(prods)
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-card__info empty:hidden'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('price-list',{'class':'price-list'})
        priceNum = nomProdPrice.text
        #print(priceNum)
        priceNum = priceNum.replace('.','')
        
        priceNum = priceNum.split('$') #--> ['\nPrecio de oferta', '19800\nPrecio normal', '22000']
        
        if len(priceNum) == 2:
            priceNum = priceNum[1]
        elif len(priceNum) == 3:
            priceNum = priceNum[2]

        priceNum = priceNum.replace(' ','')
        #print(priceNum)
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://spacionatural.cl/collections/colorantes/?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('product-card', {'class':'product-card'})
    #print(prods)
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-card__info empty:hidden'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('price-list',{'class':'price-list'})
        priceNum = nomProdPrice.text
        #print(priceNum)
        priceNum = priceNum.replace('.','')
        
        priceNum = priceNum.split('$') #--> ['\nPrecio de oferta', '19800\nPrecio normal', '22000']
        
        if len(priceNum) == 2:
            priceNum = priceNum[1]
        elif len(priceNum) == 3:
            priceNum = priceNum[2]

        priceNum = priceNum.replace(' ','')
        #print(priceNum)
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://spacionatural.cl/collections/colorantes-vegetales/?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('product-card', {'class':'product-card'})
    #print(prods)
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-card__info empty:hidden'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('price-list',{'class':'price-list'})
        priceNum = nomProdPrice.text
        #print(priceNum)
        priceNum = priceNum.replace('.','')
        
        priceNum = priceNum.split('$') #--> ['\nPrecio de oferta', '19800\nPrecio normal', '22000']
        
        if len(priceNum) == 2:
            priceNum = priceNum[1]
        elif len(priceNum) == 3:
            priceNum = priceNum[2]

        priceNum = priceNum.replace(' ','')
        #print(priceNum)
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://spacionatural.cl/collections/polvos-de-micas/?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('product-card', {'class':'product-card'})
    #print(prods)
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-card__info empty:hidden'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('price-list',{'class':'price-list'})
        priceNum = nomProdPrice.text
        #print(priceNum)
        priceNum = priceNum.replace('.','')
        
        priceNum = priceNum.split('$') #--> ['\nPrecio de oferta', '19800\nPrecio normal', '22000']
        
        if len(priceNum) == 2:
            priceNum = priceNum[1]
        elif len(priceNum) == 3:
            priceNum = priceNum[2]

        priceNum = priceNum.replace(' ','')
        #print(priceNum)
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://spacionatural.cl/collections/conservantes/?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('product-card', {'class':'product-card'})
    #print(prods)
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-card__info empty:hidden'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('price-list',{'class':'price-list'})
        priceNum = nomProdPrice.text
        #print(priceNum)
        priceNum = priceNum.replace('.','')
        
        priceNum = priceNum.split('$') #--> ['\nPrecio de oferta', '19800\nPrecio normal', '22000']
        
        if len(priceNum) == 2:
            priceNum = priceNum[1]
        elif len(priceNum) == 3:
            priceNum = priceNum[2]

        priceNum = priceNum.replace(' ','')
        #print(priceNum)
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://spacionatural.cl/collections/emulsionantes-coemulsionantes/?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('product-card', {'class':'product-card'})
    #print(prods)
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-card__info empty:hidden'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('price-list',{'class':'price-list'})
        priceNum = nomProdPrice.text
        #print(priceNum)
        priceNum = priceNum.replace('.','')
        
        priceNum = priceNum.split('$') #--> ['\nPrecio de oferta', '19800\nPrecio normal', '22000']
        
        if len(priceNum) == 2:
            priceNum = priceNum[1]
        elif len(priceNum) == 3:
            priceNum = priceNum[2]

        priceNum = priceNum.replace(' ','')
        #print(priceNum)
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://spacionatural.cl/pages/envases/?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('product-card', {'class':'product-card'})
    #print(prods)
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-card__info empty:hidden'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('price-list',{'class':'price-list'})
        priceNum = nomProdPrice.text
        #print(priceNum)
        priceNum = priceNum.replace('.','')
        
        priceNum = priceNum.split('$') #--> ['\nPrecio de oferta', '19800\nPrecio normal', '22000']
        
        if len(priceNum) == 2:
            priceNum = priceNum[1]
        elif len(priceNum) == 3:
            priceNum = priceNum[2]

        priceNum = priceNum.replace(' ','')
        #print(priceNum)
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,3):
    URL = 'https://spacionatural.cl/collections/esencias-aromaticas/?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('product-card', {'class':'product-card'})
    #print(prods)
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-card__info empty:hidden'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('price-list',{'class':'price-list'})
        priceNum = nomProdPrice.text
        #print(priceNum)
        priceNum = priceNum.replace('.','')
        
        priceNum = priceNum.split('$') #--> ['\nPrecio de oferta', '19800\nPrecio normal', '22000']
        
        if len(priceNum) == 2:
            priceNum = priceNum[1]
        elif len(priceNum) == 3:
            priceNum = priceNum[2]

        priceNum = priceNum.replace(' ','')
        #print(priceNum)
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://spacionatural.cl/collections/espesantes/?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('product-card', {'class':'product-card'})
    #print(prods)
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-card__info empty:hidden'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('price-list',{'class':'price-list'})
        priceNum = nomProdPrice.text
        #print(priceNum)
        priceNum = priceNum.replace('.','')
        
        priceNum = priceNum.split('$') #--> ['\nPrecio de oferta', '19800\nPrecio normal', '22000']
        
        if len(priceNum) == 2:
            priceNum = priceNum[1]
        elif len(priceNum) == 3:
            priceNum = priceNum[2]

        priceNum = priceNum.replace(' ','')
        #print(priceNum)
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://spacionatural.cl/collections/exfoliantes/?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('product-card', {'class':'product-card'})
    #print(prods)
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-card__info empty:hidden'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('price-list',{'class':'price-list'})
        priceNum = nomProdPrice.text
        #print(priceNum)
        priceNum = priceNum.replace('.','')
        
        priceNum = priceNum.split('$') #--> ['\nPrecio de oferta', '19800\nPrecio normal', '22000']
        
        if len(priceNum) == 2:
            priceNum = priceNum[1]
        elif len(priceNum) == 3:
            priceNum = priceNum[2]

        priceNum = priceNum.replace(' ','')
        #print(priceNum)
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://spacionatural.cl/collections/extractos-vegetales-naturales/?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('product-card', {'class':'product-card'})
    #print(prods)
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-card__info empty:hidden'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('price-list',{'class':'price-list'})
        priceNum = nomProdPrice.text
        #print(priceNum)
        priceNum = priceNum.replace('.','')
        
        priceNum = priceNum.split('$') #--> ['\nPrecio de oferta', '19800\nPrecio normal', '22000']
        
        if len(priceNum) == 2:
            priceNum = priceNum[1]
        elif len(priceNum) == 3:
            priceNum = priceNum[2]

        priceNum = priceNum.replace(' ','')
        #print(priceNum)
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://spacionatural.cl/collections/todas-las-herramientas/?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('product-card', {'class':'product-card'})
    #print(prods)
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-card__info empty:hidden'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('price-list',{'class':'price-list'})
        priceNum = nomProdPrice.text
        #print(priceNum)
        priceNum = priceNum.replace('.','')
        
        priceNum = priceNum.split('$') #--> ['\nPrecio de oferta', '19800\nPrecio normal', '22000']
        
        if len(priceNum) == 2:
            priceNum = priceNum[1]
        elif len(priceNum) == 3:
            priceNum = priceNum[2]

        priceNum = priceNum.replace(' ','')
        #print(priceNum)
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://spacionatural.cl/collections/hidrolatos/?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('product-card', {'class':'product-card'})
    #print(prods)
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-card__info empty:hidden'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('price-list',{'class':'price-list'})
        priceNum = nomProdPrice.text
        #print(priceNum)
        priceNum = priceNum.replace('.','')
        
        priceNum = priceNum.split('$') #--> ['\nPrecio de oferta', '19800\nPrecio normal', '22000']
        
        if len(priceNum) == 2:
            priceNum = priceNum[1]
        elif len(priceNum) == 3:
            priceNum = priceNum[2]

        priceNum = priceNum.replace(' ','')
        #print(priceNum)
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://spacionatural.cl/collections/hierbas-para-cosmetica/?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('product-card', {'class':'product-card'})
    #print(prods)
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-card__info empty:hidden'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('price-list',{'class':'price-list'})
        priceNum = nomProdPrice.text
        #print(priceNum)
        priceNum = priceNum.replace('.','')
        
        priceNum = priceNum.split('$') #--> ['\nPrecio de oferta', '19800\nPrecio normal', '22000']
        
        if len(priceNum) == 2:
            priceNum = priceNum[1]
        elif len(priceNum) == 3:
            priceNum = priceNum[2]

        priceNum = priceNum.replace(' ','')
        #print(priceNum)
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://spacionatural.cl/collections/leches-cosmeticas/?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('product-card', {'class':'product-card'})
    #print(prods)
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-card__info empty:hidden'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('price-list',{'class':'price-list'})
        priceNum = nomProdPrice.text
        #print(priceNum)
        priceNum = priceNum.replace('.','')
        
        priceNum = priceNum.split('$') #--> ['\nPrecio de oferta', '19800\nPrecio normal', '22000']
        
        if len(priceNum) == 2:
            priceNum = priceNum[1]
        elif len(priceNum) == 3:
            priceNum = priceNum[2]

        priceNum = priceNum.replace(' ','')
        #print(priceNum)
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://spacionatural.cl/collections/mantecas-vegetales-naturales/?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('product-card', {'class':'product-card'})
    #print(prods)
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-card__info empty:hidden'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('price-list',{'class':'price-list'})
        priceNum = nomProdPrice.text
        #print(priceNum)
        priceNum = priceNum.replace('.','')
        
        priceNum = priceNum.split('$') #--> ['\nPrecio de oferta', '19800\nPrecio normal', '22000']
        
        if len(priceNum) == 2:
            priceNum = priceNum[1]
        elif len(priceNum) == 3:
            priceNum = priceNum[2]

        priceNum = priceNum.replace(' ','')
        #print(priceNum)
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://spacionatural.cl/collections/moldes-hacer-bombas-bano/?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('product-card', {'class':'product-card'})
    #print(prods)
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-card__info empty:hidden'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('price-list',{'class':'price-list'})
        priceNum = nomProdPrice.text
        #print(priceNum)
        priceNum = priceNum.replace('.','')
        
        priceNum = priceNum.split('$') #--> ['\nPrecio de oferta', '19800\nPrecio normal', '22000']
        
        if len(priceNum) == 2:
            priceNum = priceNum[1]
        elif len(priceNum) == 3:
            priceNum = priceNum[2]

        priceNum = priceNum.replace(' ','')
        #print(priceNum)
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,4):
    URL = 'https://spacionatural.cl/collections/moldes-de-silicona/?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('product-card', {'class':'product-card'})
    #print(prods)
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-card__info empty:hidden'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('price-list',{'class':'price-list'})
        priceNum = nomProdPrice.text
        #print(priceNum)
        priceNum = priceNum.replace('.','')
        
        priceNum = priceNum.split('$') #--> ['\nPrecio de oferta', '19800\nPrecio normal', '22000']
        
        if len(priceNum) == 2:
            priceNum = priceNum[1]
        elif len(priceNum) == 3:
            priceNum = priceNum[2]

        priceNum = priceNum.replace(' ','')
        #print(priceNum)
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://spacionatural.cl/pages/tensioactivos/?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('product-card', {'class':'product-card'})
    #print(prods)
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-card__info empty:hidden'})
        #print(nomProd)
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('price-list',{'class':'price-list'})
        priceNum = nomProdPrice.text
        #print(priceNum)
        priceNum = priceNum.replace('.','')
        
        priceNum = priceNum.split('$') #--> ['\nPrecio de oferta', '19800\nPrecio normal', '22000']
        
        if len(priceNum) == 2:
            priceNum = priceNum[1]
        elif len(priceNum) == 3:
            priceNum = priceNum[2]

        priceNum = priceNum.replace(' ','')
        #print(priceNum)
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

df = pd.DataFrame({'Producto':nom, 'Precio':price, 'URL':url})
df.to_csv('spacionatural.csv', index=False, encoding='utf-8')
"""
"""
#Cooltiva
URL = 'https://cooltiva.cl/collections/nuestros-productos'
page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)
prods = soup.find_all('div', {'class':'hp-title'})
for itemProd in prods:
    nomProd = itemProd.find('a').find('span', {'class':'indiv-product-title-text'})
    #print(nomProd.text)
    nomProdtext = itemProd.find('a')
    nomProdname = nomProdtext.text
    nomProd = nomProd.text
    nomProd = nomProd.replace(',','')
    nomProd = nomProd.replace('"','')
    nomProd = nomProd.replace('  ','')
    nomProd = nomProd.replace('   ','')
    nomProd = nomProd.replace('\n','')
    nomProdname = nomProdname.replace('  ','')
    nomProdname = nomProdname.replace('   ','')
    nomProdname = nomProdname.replace('\n','')
    #print(nomProd)
    nom.append(nomProd)
    #print(nomProdtext['href'])
    url.append(nomProdtext['href'])
    nomProdPrice = itemProd.find('span',{'class':'money'})
    priceNum = nomProdPrice.text
    priceNum = priceNum.replace('.','')
    priceNum = priceNum.replace('$','')
    priceNum = priceNum.replace(' ','')
    #print(nomProdPrice.text)
    price.append(re.findall("\d+", priceNum)[0])

df = pd.DataFrame({'Producto':nom, 'Precio':price, 'URL':url})
df.to_csv('cooltiva.csv', index=False, encoding='utf-8')
"""
"""
#Anterior pagina Herbolario ELIMINADA!
URL = 'https://www.herbolario.cl/lista-de-precios'
page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)
table = soup.find('tbody')
nomProd = table.findAll('tr')
for lista in nomProd:
    nomProdname = lista.find_all('td')
    #print(nomProdname)
    nomProdnametext = nomProdname[0].text.strip()
    #print(nomProdnametext)
    nomProdPrice = nomProdname[-1].get_text()
    #print(nomProdPrice)
    nom.append(nomProdnametext)
    price.append(nomProdPrice)
df = pd.DataFrame({'Producto':nom, 'Precio':price})
df.to_csv('herbolario.csv', index=False, encoding='utf-8')
"""
"""
#Herbolario
for pag in range(1,2):
    URL = 'https://www.herbolario.cl/aceites-esenciales?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    prods = soup.find_all('div', {'class':'product-block col-12 col-sm-6 col-md-4 col-lg-3 trsn'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-block__info'})
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'product-block__price product-block__price--discount'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        if len(priceNum) > 5:
            priceNum = priceNum.replace('$',' - ')
        else:
            priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://www.herbolario.cl/mantecas-y-ceras?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    prods = soup.find_all('div', {'class':'product-block col-12 col-sm-6 col-md-4 col-lg-3 trsn'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-block__info'})
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'product-block__price'})
        priceNum = nomProdPrice.text
        #print(priceNum) Desde Precio
        priceNum = priceNum.replace('.','')
        if len(priceNum) > 5:
            priceNum = priceNum.replace('$',' - ')
        else:
            priceNum = priceNum.replace('$','')
        #print(priceNum)
        priceNum = priceNum.replace(' ','')
        #print(("\d+", priceNum)[0])
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://www.herbolario.cl/aceites?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    prods = soup.find_all('div', {'class':'product-block col-12 col-sm-6 col-md-4 col-lg-3 trsn'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-block__info'})
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'product-block__price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        if len(priceNum) > 5:
            priceNum = priceNum.replace('$',' - ')
        else:
            priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,3):
    URL = 'https://www.herbolario.cl/activos?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    prods = soup.find_all('div', {'class':'product-block col-12 col-sm-6 col-md-4 col-lg-3 trsn'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-block__info'})
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'product-block__price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        if len(priceNum) > 5:
            priceNum = priceNum.replace('$',' - ')
        else:
            priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,3):
    URL = 'https://www.herbolario.cl/activos-y-extractos/extractos?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    prods = soup.find_all('div', {'class':'product-block col-12 col-sm-6 col-md-4 col-lg-3 trsn'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-block__info'})
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'product-block__price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        if len(priceNum) > 5:
            priceNum = priceNum.replace('$',' - ')
        else:
            priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://www.herbolario.cl/aditivos-en-polvo?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    prods = soup.find_all('div', {'class':'product-block col-12 col-sm-6 col-md-4 col-lg-3 trsn'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-block__info'})
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'product-block__price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        if len(priceNum) > 5:
            priceNum = priceNum.replace('$',' - ')
        else:
            priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,3):
    URL = 'https://www.herbolario.cl/personal-care?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    prods = soup.find_all('div', {'class':'product-block col-12 col-sm-6 col-md-4 col-lg-3 trsn'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-block__info'})
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'product-block__price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        if len(priceNum) > 5:
            priceNum = priceNum.replace('$',' - ')
        else:
            priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://www.herbolario.cl/infantiles?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    prods = soup.find_all('div', {'class':'product-block col-12 col-sm-6 col-md-4 col-lg-3 trsn'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-block__info'})
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'product-block__price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        if len(priceNum) > 5:
            priceNum = priceNum.replace('$',' - ')
        else:
            priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://www.herbolario.cl/hipo-alergenicas?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    prods = soup.find_all('div', {'class':'product-block col-12 col-sm-6 col-md-4 col-lg-3 trsn'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-block__info'})
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'product-block__price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        if len(priceNum) > 5:
            priceNum = priceNum.replace('$',' - ')
        else:
            priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://www.herbolario.cl/oleo-fragancias?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    prods = soup.find_all('div', {'class':'product-block col-12 col-sm-6 col-md-4 col-lg-3 trsn'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-block__info'})
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'product-block__price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        if len(priceNum) > 5:
            priceNum = priceNum.replace('$',' - ')
        else:
            priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://www.herbolario.cl/saborizantes?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    prods = soup.find_all('div', {'class':'product-block col-12 col-sm-6 col-md-4 col-lg-3 trsn'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-block__info'})
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'product-block__price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        if len(priceNum) > 5:
            priceNum = priceNum.replace('$',' - ')
        else:
            priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://www.herbolario.cl/fundacion-y-filler?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    prods = soup.find_all('div', {'class':'product-block col-12 col-sm-6 col-md-4 col-lg-3 trsn'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-block__info'})
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'product-block__price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        if len(priceNum) > 5:
            priceNum = priceNum.replace('$',' - ')
        else:
            priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://www.herbolario.cl/colorantes-liquidos?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    prods = soup.find_all('div', {'class':'product-block col-12 col-sm-6 col-md-4 col-lg-3 trsn'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-block__info'})
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'product-block__price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        if len(priceNum) > 5:
            priceNum = priceNum.replace('$',' - ')
        else:
            priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://www.herbolario.cl/conservantes-y-reguladores-del-ph?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    prods = soup.find_all('div', {'class':'product-block col-12 col-sm-6 col-md-4 col-lg-3 trsn'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-block__info'})
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'product-block__price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        if len(priceNum) > 5:
            priceNum = priceNum.replace('$',' - ')
        else:
            priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://www.herbolario.cl/emulsionantes?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    prods = soup.find_all('div', {'class':'product-block col-12 col-sm-6 col-md-4 col-lg-3 trsn'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-block__info'})
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'product-block__price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        if len(priceNum) > 5:
            priceNum = priceNum.replace('$',' - ')
        else:
            priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://www.herbolario.cl/gomas?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    prods = soup.find_all('div', {'class':'product-block col-12 col-sm-6 col-md-4 col-lg-3 trsn'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-block__info'})
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'product-block__price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        if len(priceNum) > 5:
            priceNum = priceNum.replace('$',' - ')
        else:
            priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://www.herbolario.cl/bases?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    prods = soup.find_all('div', {'class':'product-block col-12 col-sm-6 col-md-4 col-lg-3 trsn'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-block__info'})
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'product-block__price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        if len(priceNum) > 5:
            priceNum = priceNum.replace('$',' - ')
        else:
            priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://www.herbolario.cl/tensioactivos?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    prods = soup.find_all('div', {'class':'product-block col-12 col-sm-6 col-md-4 col-lg-3 trsn'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-block__info'})
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'product-block__price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        if len(priceNum) > 5:
            priceNum = priceNum.replace('$',' - ')
        else:
            priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://www.herbolario.cl/botellas-pet?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    prods = soup.find_all('div', {'class':'product-block col-12 col-sm-6 col-md-4 col-lg-3 trsn'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-block__info'})
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'product-block__price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        if len(priceNum) > 5:
            priceNum = priceNum.replace('$',' - ')
        else:
            priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://www.herbolario.cl/tapas-y-bombas?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    prods = soup.find_all('div', {'class':'product-block col-12 col-sm-6 col-md-4 col-lg-3 trsn'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-block__info'})
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'product-block__price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        if len(priceNum) > 5:
            priceNum = priceNum.replace('$',' - ')
        else:
            priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://www.herbolario.cl/potes-y-envases-pet?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    prods = soup.find_all('div', {'class':'product-block col-12 col-sm-6 col-md-4 col-lg-3 trsn'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-block__info'})
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'product-block__price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        if len(priceNum) > 5:
            priceNum = priceNum.replace('$',' - ')
        else:
            priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://www.herbolario.cl/envases-de-vidrio?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    prods = soup.find_all('div', {'class':'product-block col-12 col-sm-6 col-md-4 col-lg-3 trsn'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-block__info'})
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'product-block__price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        if len(priceNum) > 5:
            priceNum = priceNum.replace('$',' - ')
        else:
            priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://www.herbolario.cl/moldes?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    prods = soup.find_all('div', {'class':'product-block col-12 col-sm-6 col-md-4 col-lg-3 trsn'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-block__info'})
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'product-block__price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        if len(priceNum) > 5:
            priceNum = priceNum.replace('$',' - ')
        else:
            priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://www.herbolario.cl/accesorios?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    prods = soup.find_all('div', {'class':'product-block col-12 col-sm-6 col-md-4 col-lg-3 trsn'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'product-block__info'})
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('div',{'class':'product-block__price'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        if len(priceNum) > 5:
            priceNum = priceNum.replace('$',' - ')
        else:
            priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        price.append(re.findall("\d+", priceNum)[0])

#print("Len nom", len(nom))
#print("Len format", len(format))
#print("Len price", len(price))
#print("Len url", len(url))

df = pd.DataFrame({'Producto':nom, 'Precio':price, 'URL':url})
df.to_csv('herbolario.csv', index=False, encoding='utf-8')
"""
"""
#De castanas y amores
for pag in range(1,7):
    URL = 'https://www.xn--decastaasyamores-dub.cl/aceites?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'caption'})
    for itemProd in prods:
        nomProd = itemProd.find('a').get_text()
        #print(nomProd)
        nomProdtext = itemProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #rint(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('span',{'class':'product-block-list'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,6):
    URL = 'https://www.xn--decastaasyamores-dub.cl/materias-primas?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'caption'})
    for itemProd in prods:
        nomProd = itemProd.find('a').get_text()
        #print(nomProd)
        nomProdtext = itemProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #rint(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('span',{'class':'product-block-list'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,5):
    URL = 'https://www.xn--decastaasyamores-dub.cl/productos-terminados?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'caption'})
    for itemProd in prods:
        nomProd = itemProd.find('a').get_text()
        #print(nomProd)
        nomProdtext = itemProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #rint(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('span',{'class':'product-block-list'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,3):
    URL = 'https://www.xn--decastaasyamores-dub.cl/flores-petalos-y-frutas-secas?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'caption'})
    for itemProd in prods:
        nomProd = itemProd.find('a').get_text()
        #print(nomProd)
        nomProdtext = itemProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #rint(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('span',{'class':'product-block-list'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,4):
    URL = 'https://www.xn--decastaasyamores-dub.cl/hidrolatos?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'caption'})
    for itemProd in prods:
        nomProd = itemProd.find('a').get_text()
        #print(nomProd)
        nomProdtext = itemProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #rint(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('span',{'class':'product-block-list'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,8):
    URL = 'https://www.xn--decastaasyamores-dub.cl/moldes-y-utensilios?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'caption'})
    for itemProd in prods:
        nomProd = itemProd.find('a').get_text()
        #print(nomProd)
        nomProdtext = itemProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #rint(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('span',{'class':'product-block-list'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,6):
    URL = 'https://www.xn--decastaasyamores-dub.cl/envases?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'caption'})
    for itemProd in prods:
        nomProd = itemProd.find('a').get_text()
        #print(nomProd)
        nomProdtext = itemProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #rint(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('span',{'class':'product-block-list'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://www.xn--decastaasyamores-dub.cl/suplementos-naturales?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'caption'})
    for itemProd in prods:
        nomProd = itemProd.find('a').get_text()
        #print(nomProd)
        nomProdtext = itemProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #rint(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('span',{'class':'product-block-list'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,3):
    URL = 'https://www.xn--decastaasyamores-dub.cl/insumos-para-velas?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'caption'})
    for itemProd in prods:
        nomProd = itemProd.find('a').get_text()
        #print(nomProd)
        nomProdtext = itemProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #rint(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('span',{'class':'product-block-list'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

df = pd.DataFrame({'Producto':nom, 'Precio':price, 'URL':url})
df.to_csv('decastanasyamores.csv', index=False, encoding='utf-8')
"""
"""
#Anahata
for pag in range(1,54):
    URL = 'https://anahataproductosnaturales.cl/tienda/page/'+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'productCode'})
    for itemProd in prods:
        nomProd = itemProd.find('div', {'class':'titleCode'})
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('bdi')
        if nomProdPrice is not None:
            priceNum = nomProdPrice.text
            priceNum = priceNum.replace('.','')
            priceNum = priceNum.replace('$','')
            priceNum = priceNum.replace(' ','')
            #print(nomProdPrice.text)
            price.append(re.findall("\d+", priceNum)[0])
        else:
            price.append('')

        nomChecked = (itemProd.find('input',{'class':'input-radio','checked':'checked'}))
        if nomChecked:
            nomCheckedPar = nomChecked.parent
            nomCheckedText = nomCheckedPar.find('span', {'class':'radio-label'})
            if nomCheckedText:
                #print(nomCheckedText.text)
                format.append(nomCheckedText.text)
            else: 
                format.append('')
        else:
            format.append('')

df = pd.DataFrame({'Producto':nom, 'Precio':price, 'URL':url})
df.to_csv('anahata.csv', index=False, encoding='utf-8')
"""
"""
#Sororite  ELIMINADA!
for pag in range(1,2):
    URL = 'https://sororiteinsumos.cl/tienda/cosmetica-natural?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'card-body'})
    for itemProd in prods:
        nomProd = itemProd.find('h6', {'class':'card-title'})
        nomProdtext = itemProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('span', id="label_precio")
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://sororiteinsumos.cl/tienda/aceites-y-mantecas?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'card-body'})
    for itemProd in prods:
        nomProd = itemProd.find('h6', {'class':'card-title'})
        nomProdtext = itemProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('span', id="label_precio")
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://sororiteinsumos.cl/tienda/aceites-esenciales?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'card-body'})
    for itemProd in prods:
        nomProd = itemProd.find('h6', {'class':'card-title'})
        nomProdtext = itemProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('span', id="label_precio")
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://sororiteinsumos.cl/tienda/bases?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'card-body'})
    for itemProd in prods:
        nomProd = itemProd.find('h6', {'class':'card-title'})
        nomProdtext = itemProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('span', id="label_precio")
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,3):
    URL = 'https://sororiteinsumos.cl/tienda/colores-y-pigmentos?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'card-body'})
    for itemProd in prods:
        nomProd = itemProd.find('h6', {'class':'card-title'})
        nomProdtext = itemProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('span', id="label_precio")
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,5):
    URL = 'https://sororiteinsumos.cl/tienda/otros-insumos?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'card-body'})
    for itemProd in prods:
        nomProd = itemProd.find('h6', {'class':'card-title'})
        nomProdtext = itemProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('span', id="label_precio")
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://sororiteinsumos.cl/tienda/envases?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'card-body'})
    for itemProd in prods:
        nomProd = itemProd.find('h6', {'class':'card-title'})
        nomProdtext = itemProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('span', id="label_precio")
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

for pag in range(1,2):
    URL = 'https://sororiteinsumos.cl/tienda/emulsionantes-y-tensioactivos?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'card-body'})
    for itemProd in prods:
        nomProd = itemProd.find('h6', {'class':'card-title'})
        nomProdtext = itemProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('span', id="label_precio")
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

df = pd.DataFrame({'Producto':nom, 'Precio':price, 'URL':url})
df.to_csv('sororite.csv', index=False, encoding='utf-8')
"""
"""
#Emporio naranja (Firewall)
for pag in range(1,2):
    URL = 'https://www.emporionaranja.cl/tienda/page/'+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'caption'})
    for itemProd in prods:
        nomProd = itemProd.find('a').get_text()
        #print(nomProd)
        nomProdtext = itemProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('bdi')
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])

df = pd.DataFrame({'Producto':nom, 'Precio':price, 'URL':url})
df.to_csv('emporionaranja.csv', index=False, encoding='utf-8')
"""