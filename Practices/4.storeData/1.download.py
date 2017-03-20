from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

baseUrl = "http://pythonscraping.com"
downloadDirectory = "download"

html = urlopen(baseUrl)
bsObj = BeautifulSoup(html,"lxml")
# find logo image
# imageLocation = bsObj.find("a",{"id":"logo"}).find("img")["src"]
# urlretrieve(imageLocation,"logo.jpg")


def getAbsoluteUrl(baseUrl,source):
    if source.startswith("http://www."):
        url = "http://" + source[11:]
    elif source.startswith("http://"):
        url = source
    elif source.startswith("www."):
        url = source[4:]
        url = "http://" + source
    else:
        url = baseUrl + "/" + source
    if baseUrl not in url:
        return None
    return url
# return value: e.g.,   http://pythonscraping.com/sites/default/files/lrg_0.jpg
#                       http://pythonscraping.com/img/lrg%20(1).jpg


def getDownLoadPath(baseUrl,absoluteUrl,downloadDirectory):
    path = absoluteUrl.replace("www.","")
    path = path.replace(baseUrl,"")
    path = downloadDirectory + path
    directory = os.path.dirname(path)

    if not os.path.exists(directory):
        os.makedirs(directory)

    print(path)
    return path



#downloadList = bsObj.findAll("a").find("img")["src"]
downloadList = bsObj.findAll("img")

for download in downloadList:
    fileUrl = getAbsoluteUrl(baseUrl,download["src"])
    if fileUrl is not None:
        print(fileUrl)
        downloadPath = getDownLoadPath(baseUrl,fileUrl,downloadDirectory)
        urlretrieve(fileUrl, downloadPath)
        print("---------------------------")
