from urllib.request import urlopen
from bs4 import BeautifulSoup

# get the text directly from html
# tags are not needed, and cannot be used anymore
textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")

print(str(textPage.read(),'utf-8'))
# russian encoded with utf-8. Be careful with foreign language (that is not English or
# dont use Latin character set)
