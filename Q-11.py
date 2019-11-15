import requests
from bs4 import BeautifulSoup

#Web Scraping (100 movies)
result=requests.get("https://www.imdb.com/list/ls006266261/")
soup=BeautifulSoup(result.text,features="html.parser")

l=soup.find_all('h3',{'class':'lister-item-header'})
m_name=[]
for x in l:
    for y in x.find_all('a'):
        m_name.append(y.text)
print(m_name)
