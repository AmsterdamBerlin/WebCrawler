from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

# split the task into two parts:
# 1. get internal links:  on the same website or domain
# 2. get external links:  outside the same website or domain


def getInLinks(bsObj,inUrl):
    inLinks = []
    for link in bsObj.findAll("a", href = re.compile("^(|.*" + inUrl + ")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in inLinks:
                inLinks.append(link.attrs['href'])
    return inLinks

def getExLinks(bsObj,exUrl):
    exLinks = []
    for link in bsObj.findAll("a", href = re.compile("^(http|www)((?!" + exUrl + ").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in exLinks:
                exLinks.append(link.attrs['href'])
    return exLinks

def splitAddress(address):
    addressParts = address.replace("http://","").split("/")
    return addressParts
#  turning a http address to a list of string
#  http://stackoverflow.com/questions/20507139/python-split-replace =>
#  ['stackoverflow.com', 'questions', '20507139', 'python-split-replace']

def getRandomExLink(newPage):
    html = urlopen(newPage)
    bsObj = BeautifulSoup(html,"lxml")
    exLinks = getExLinks(bsObj,splitAddress(newPage)[0]) # get the first string of web domain
    if len(exLinks) == 0:
        inLinks = getInLinks(newPage)
        return getRandomExLink(inLinks[random.randint(0,len(inLinks)-1)])
    else:
        return exLinks[random.randint(0,len(exLinks)-1)]

def followExOnly(newPage):
    exLink = getRandomExLink(newPage)
    print("random external link is: " + exLink)
    followExOnly(exLink)

#followExOnly("http://oreilly.com")


allExLinks = set()
allInLinks = set()


def getAllExLinks(newPage):
    html = urlopen(newPage)
    bsObj = BeautifulSoup(html,"lxml")
    inLinks = getInLinks(bsObj,splitAddress(newPage)[0])
    exLinks = getExLinks(bsObj,splitAddress(newPage)[0])

    for link in exLinks:
        if link not in allExLinks:
            print("get an external link: " + link)
            allExLinks.add(link)

    for link in inLinks:
        if link not in allInLinks:
            print("get an internal link: " + link)
            allInLinks.add(link)
            getAllExLinks(link)

getAllExLinks("http://oreilly.com")
# incomplete version as the code cannot translate internal link to a proper website address
# e.g., links that begin with a "/" : "//cdn.oreillystatic.com/assets/css/norm-layout-170202.css"
# hence, exception handling is vital
