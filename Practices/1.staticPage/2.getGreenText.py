from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html,"lxml")

# find all the text within the SPAN with CLASS GREEN
# tagName, NOTE: tagAttributes
nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList:
    print(name.get_text()) #in order to separate the content from the tag ; it is the last thing to do
