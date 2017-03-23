from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import requests
import os
import re
import time

path = "./imagesUrl"
Urls = "url.txt"

class downloading:
    def __init__(self,html):
        self.html = html
        self.bsObj = BeautifulSoup(self.html,"lxml")
        self.downloadList = self.bsObj.findAll("img",{"src":re.compile("http://ww")})
        self.image_urls =[]

        filepath = os.path.join(path, Urls)
        if not os.path.exists(path):
            os.makedirs(path)

        writeUrl = open(filepath, 'w')
        for link in self.downloadList:
            # change small size to large size
            url = link['src'].replace("small","large")
            self.image_urls.append(url)
            # write the url links down in a text file
            writeUrl.write(url)
            writeUrl.write("\n")
        writeUrl.close()
        print("links are stored")

    def __retrieve(self):
        for i, url in  enumerate(self.image_urls):
            urlretrieve(url, os.path.join(path, str(i)+".jpg")) #403 block
            time.sleep(1) # to prevent from 403 block

        print("images are stored")

    def getImages(self):
        self.__retrieve()
