import requests
from bs4 import BeautifulSoup

def getSoup(url, header):
    response = requests.get(url, headers=header)
    return BeautifulSoup(response.text, "html.parser")

def getText(str):
    item = ''
    i = 0
    while str[i] != '>':
         i += 1
    i += 1
    while str[i] != '<':
        item += str[i]
        i+=1
    return item

def scrapeDrawNike():
    url = 'https://www.nike.com.hk/draw/list.htm'
    soup = getSoup(url, {})
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
        products['Nike ' + str(i+1)] = (items[i], colorways[i], prices[i])
    return products

def scrapeYeezys():
    url = 'https://www.adidas.com/us/yeezy'
    header = {
        'User-Agent': 'My User Agent 1.0', 
        'From': 'youremail@domain.com'
    } 
    soup = getSoup(url, header)
    products = {}
    count = 1
    for i in soup.findAll('title'):
        products['Adidas '+ str(count)] = getText(str(i))
        count += 1
    return products

def scrapeJUICE():
    url = 'https://juicestore.com/blogs/editorial/tagged/raffle'
    soup = getSoup(url, {})
    products = {}
    productList = []
    dateList = []
    for i in soup.findAll('h2'):
        tempName = getText(str(i))
        if 'Raffle' in tempName:
            start = 0
            while tempName[start] != ':':
                start += 1
            start = start + 2
            productList.append(tempName[start:])
    for i in soup.findAll('time'):
        dateList.append(getText(str(i)))
    for i in range(len(productList)):
        products['Juice '+ str(i+1)] = (productList[i], dateList[i])
    return products

nikeProducts = scrapeDrawNike()
yeezyProducts = scrapeYeezys()
juiceRaffles = scrapeJUICE()
f = open("ProductsList.txt","w")
f.truncate(0)
f.write('Nike Lucky Draw Products for Today:\n')
for i in nikeProducts:
    f.write(str(nikeProducts[i][0]).lower() + ' of colorway '+str(nikeProducts[i][1]).lower() + ', release date on '+str(str(nikeProducts[i][2])))
    f.write('\n')
f.write('--------------------------------------------------\n')
f.write('Upcoming Yeezy Release:\n')
for i in yeezyProducts:
    f.write(str(yeezyProducts[i]))
    f.write('\n')
f.write('--------------------------------------------------\n')
f.write('Recent Juice Store Raffles:\n')
for i in juiceRaffles:
    f.write(str(juiceRaffles[i][0]) + ', news released on '+ str(juiceRaffles[i][1]))
    f.write('\n')
f.close()



