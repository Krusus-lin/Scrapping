from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

nom=[]
format=[]
price=[]
url=[]

#Spacionatural
for pag in range(1,6):
    URL = 'https://spacionatural.cl/aceites-mantecas-y-ceras/?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'product-description'})
    for itemProd in prods:
        nomProd = itemProd.find('h3', {'class':'product-title'})
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('span',{'class':'money'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])
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

#print("Len nom", len(nom))
#print("Len format", len(format))
#print("Len price", len(price))
#print("Len url", len(url))

for pag in range(1,4):
    URL = 'https://spacionatural.cl/bases/?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'product-description'})
    for itemProd in prods:
        nomProd = itemProd.find('h3', {'class':'product-title'})
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('span',{'class':'money'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])
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

for pag in range(1,35):
    URL = 'https://spacionatural.cl/insumos/?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'product-description'})
    for itemProd in prods:
        nomProd = itemProd.find('h3', {'class':'product-title'})
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('span',{'class':'money'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])
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

for pag in range(1,5):
    URL = 'https://spacionatural.cl/envases/?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'product-description'})
    for itemProd in prods:
        nomProd = itemProd.find('h3', {'class':'product-title'})
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('span',{'class':'money'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])
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

for pag in range(1,4):
    URL = 'https://spacionatural.cl/productos-spa/?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'product-description'})
    for itemProd in prods:
        nomProd = itemProd.find('h3', {'class':'product-title'})
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('span',{'class':'money'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])
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

for pag in range(1,2):
    URL = 'https://spacionatural.cl/kits-para-aprender/?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    prods = soup.find_all('div', {'class':'product-description'})
    for itemProd in prods:
        nomProd = itemProd.find('h3', {'class':'product-title'})
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('span',{'class':'money'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])
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
            
for pag in range(1,3):
    URL = 'https://spacionatural.cl/insumos-para-velas/?page='+str(pag)
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    print("Pagina: "+str(pag))
    soup = BeautifulSoup(page.content, 'html.parser')
    prods = soup.find_all('div', {'class':'product-description'})
    for itemProd in prods:
        nomProd = itemProd.find('h3', {'class':'product-title'})
        nomProdtext = nomProd.find('a')
        nomProdname = nomProdtext.text
        nomProdname = nomProdname.replace('  ','')
        nomProdname = nomProdname.replace('   ','')
        nomProdname = nomProdname.replace('\n','')
        #print(nomProdtext.text)
        nom.append(nomProdname)
        #print(nomProdtext['href'])
        url.append(nomProdtext['href'])
        nomProdPrice = itemProd.find('span',{'class':'money'})
        priceNum = nomProdPrice.text
        priceNum = priceNum.replace('.','')
        priceNum = priceNum.replace('$','')
        priceNum = priceNum.replace(' ','')
        #print(nomProdPrice.text)
        price.append(re.findall("\d+", priceNum)[0])
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

df = pd.DataFrame({'Producto':nom, 'Formato':format, 'Precio':price, 'URL':url})
df.to_csv('spacionatural.csv', index=False, encoding='utf-8')

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