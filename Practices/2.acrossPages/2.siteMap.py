from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import re

# collects all pages in wikipedia; it leads to space explosion
pages = set()
def getPages(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html,"lxml")
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #We have encountered a new page
                newPage = link.attrs['href']
                print("----------------------\n" + newPage)
                pages.add(newPage)
                getPages(newPage)

getPages("")
