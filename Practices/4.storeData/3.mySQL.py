import pymysql
from urllib.request import urlopen
from bs4 import BeautifulSoup
from bs4 import re
import datetime
import random

# MySQL is a complicated topic. I just took a glance at it.
 
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Berlin2016', db='mysql',charset='utf8')

cur = conn.cursor()
cur.execute("USE scraping")

def store(title,content):
    cur.execute("INSERT INTO pages (title, content) VALUES (\"%s\",\"%s\")",(title,content))
    cur.connection.commit()

def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html,"lxml")
    title = bsObj.find("h1").get_text()
    print(title)
    content = bsObj.find("div",{"id":"mw-content-text"}).find("p").get_text()
    print(content)
    store(title,content)
    return bsObj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/kevin_Bacon")

i = 5
try:
    while i > 0:
        newArticle = links[random.randint(0,len(links)-1)].attrs["href"]
        print(newArticle)
        links = getLinks(newArticle)
        i = i - 1
finally:
    cur.close()
    conn.close()
