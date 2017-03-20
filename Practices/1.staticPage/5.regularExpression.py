from urllib.request import urlopen
from bs4 import BeautifulSoup
from bs4 import re

# using regular experssion to match target
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,"lxml")
images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts\/img.*.jpg")})
for image in images:
    print(image["src"])

# using attrs to find the attribute of a tag directly
for img in bsObj.findAll("img"):
    print(img.attrs["src"])
