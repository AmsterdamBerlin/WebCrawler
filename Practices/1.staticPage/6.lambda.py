from urllib.request import urlopen
from bs4 import BeautifulSoup
from bs4 import re

# using regular experssion to match target
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,"lxml")

# lambda function used for specific goal
###################################################
# The only restriction is that these functions must take a tag object as an argument
# and return a boolean
tags_2 = bsObj.findAll(lambda tag: len(tag.attrs) == 2)
# find tag that has two attributes.
# the length of a tag means how deep its structure is
for Tag in tags_2:
    print(Tag)
    print(len(Tag))
    print("\n")
