import requests
import urllib.request
import time
from bs4 import BeautifulSoup
def getText(str):
    item = ''
    i = 0
    while str[i]!= '>':
         i +=1
    i+=1
    while str[i]!='<':
        item +=str[i]
        i+=1
    return item
def scrape():
    url = 'https://www.nike.com.hk/draw/list.htm'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    soup.findAll('p')
    colorways = []
    items = []
    prices = []
    for i in soup.findAll('p'):
        temp = str(i)
        if 'tn_n' in temp:
            items.append(getText(temp))
        if 'tn_s' in temp:
            colorways.append(getText(temp))
        if 'tn_p' in temp:
            prices.append(getText(temp))
    products = {}
    for i in range(len(items)):
        products[items[i]] = (colorways[i], prices[i])
    return products
products = scrape()
f = open("shoeList.txt","w")
f.truncate(0)
for i in products:
    f.write( str(i) + ':' +str(products[i]) )
    f.write('\n')
f.close()

    
    


