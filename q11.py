'''Python Assignment Q-11'''
import requests
from bs4 import BeautifulSoup

#Web Scraping (100 movies)
RESULT = requests.get("https://www.imdb.com/list/ls006266261/")
SOUP = BeautifulSoup(RESULT.text, features="html.parser")

HTML_CODE = SOUP.find_all('h3', {'class' : 'lister-item-header'})
EMPTY_LIST = []
for x in HTML_CODE:
    for y in x.find_all('a'):
        EMPTY_LIST.append(y.text)
print(EMPTY_LIST)
