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
        # ---- collect urls of images that are going to be downloaded
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
            response = requests.get(url)
            image = response.content
            with open(os.path.join(path, str(i)+".jpg"),"wb") as image_object:
                image_object.write(image)
        print("images are stored")

    def getImages(self):
        self.__retrieve()
