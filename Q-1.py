import pymysql
import requests
from bs4 import BeautifulSoup

#Web Scraping (100 movies)
result  =  requests.get("https://www.imdb.com/list/ls006266261/")
soup  =  BeautifulSoup(result.text, features = "html.parser")

l = soup.find_all('h3',{'class':'lister-item-header'})
m_name = []
for x in l:
    for y in x.find_all('a'):
        m_name.append(y.text)
        
m_rate = []      
r = soup.find_all('div',{'class':'ipl-rating-star small'})
for x in r:
    for y in x.find_all("span",{'class':'ipl-rating-star__rating'}):
        m_rate.append(y.text)
print("Web Scraping Done!!!")

#LocalHost Database:
mydb  =  pymysql.connect(
  host = "localhost",
  user = "testuser",
  passwd = "test123"
)
mycursor  =  mydb.cursor()
mycursor.execute("DROP DATABASE IF EXISTS MOVIESDB")
mycursor.execute("CREATE DATABASE MOVIESDB")
mydb.close()
print("Database created!!!")

db  =  pymysql.connect("localhost","root","Naitik@19","MOVIESDB")
cursor  =  db.cursor()

#cursor.execute("DROP TABLE IF EXISTS movies")

cursor.execute("CREATE TABLE movies (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), raiting VARCHAR(255))")

sql  =  "INSERT INTO movies (name, raiting) VALUES (%s, %s)"
l = len(m_name)
i = 0
while(l != 0):
    val = (m_name[i],m_rate[i])
    cursor.execute(sql, val)
    i = i+1
    l = l-1

db.commit()
print("Data Stored!!!")

def fetch():
    cursor.execute("select * from movies")
    for row in cursor.fetchall():
        yield row
print(list(fetch()))
