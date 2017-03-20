from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):   # gaurantee the reliability
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None # The page is not found on the server / or the server is not found
    try:
        bsObj = BeautifulSoup(html.read(),"lxml")
        title = bsObj.body.h1 # searching for tag
    except AttributeError as e:
        return None # tag of Object is not found
    return title

title = getTitle("http://www.pythonscraping.com/exercises/exercise1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)
