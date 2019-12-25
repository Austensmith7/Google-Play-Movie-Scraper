from bs4 import BeautifulSoup
import requests
import pandas
URL = "https://play.google.com/store/movies/collection/cluster?clp=6gIjIiEKG3Byb21vdGlvbl9tb3ZpZXNfdG9wc2VsbGluZxAHGAQ%3D:S:ANO1ljIFa3o&gsr=CibqAiMiIQobcHJvbW90aW9uX21vdmllc190b3BzZWxsaW5nEAcYBA%3D%3D:S:ANO1ljJIt30&hl=en_US"
r = requests.get(URL)

movieNames = []
moviePrices = []
movieRatings = []

page_soup = BeautifulSoup(r.content, 'html.parser')
#Start of dig
alphabet = page_soup.find('div', {'id':'fcxH9b'})

a = alphabet.find('div',{'class':'WpDbMd'})

b = a.find('c-wiz',{'class':'zQTmif SSPGKf I3xX3c'})

c = b.find('div', {'class':'T4LgNb'})

d = c.find('c-wiz')

e = d.find('div',{'class':'N4FjMb'})

f = e.find('c-wiz',{'data-node-index':'1;0'})

g = f.find('c-wiz',{'class':'UBeTzd Ubi8Z'})

h = g.find('c-wiz',{'data-node-index':'12;0'})

i = h.find('div',{'class':'Ktdaqe'})

j = i.find('div',{'class':'ZmHEEd'})

#Loop to find Movie Names
movieList = j.findAll('div', {'class':'ImZGtf mpg5gc'})
for movie in movieList:

    k = movie.find('c-wiz')

    l = k.find('div',{'class':'uMConb V2Vq5e POHYmb-T8c9cb YEDFMc-T8c9cb y1APZe-T8c9cb q9QOMe'})

    m = l.find('div',{'class':'Vpfmgd'})

    n = m.find('div',{'class':'RZEgze'})

    o = n.find('div',{'class':'vU6FJ p63iDd'})

    p = o.find('div',{'class':'k6AFYd'})

    q = p.find('div',{'class':'bQVA0c'})

    r = q.find('div',{'class':'PODJt'})

    s = r.find('div',{'class':'kCSSQe'})

    t = s.find('div',{'class':'b8cIId ReQCgd Q9MA7b'})

    u = t.find('a')

    v = u.find('div',{'WsMG1c nnK0zc'}).text

    movieNames.append(v)

#Loop to find Prices
priceList = j.findAll('div', {'class':'ImZGtf mpg5gc'})
for price in priceList:

    k = price.find('c-wiz')

    l = k.find('div',{'class':'uMConb V2Vq5e POHYmb-T8c9cb YEDFMc-T8c9cb y1APZe-T8c9cb q9QOMe'})

    m = l.find('div',{'class':'Vpfmgd'})

    n = m.find('div',{'class':'RZEgze'})

    o = n.find('div',{'class':'vU6FJ p63iDd'})

    p = o.find('div',{'class':'k6AFYd'})

    q = p.find('div',{'class':'Z2nl8b'})

    r = q.find('div',{'class':'PODJt'})

    s = r.find('div',{'class':'zYPPle'})

    t = s.find('div')

    u = t.find('button',{'class':'svCDYe aYzfud YpSFl'})

    v = u.find('div',{'LCATme'})

    q = v.find('span',{'VfPpfd ZdBevf i5DZme'}).text
    moviePrices.append(q)



df = pandas.DataFrame({'Movie Name':movieNames,'Price':moviePrices})
df.to_csv('database.csv', index=False, encoding='utf-8')












