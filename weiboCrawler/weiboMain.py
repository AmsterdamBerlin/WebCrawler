from getPage import *
from download import *

username =    #"makeAmericaGreatAgain@qq.com"
password =           #"********"

targetUser = 
targetUrl =


onlyTxt = False

def weiboCrawler(username,password,targetUser,targetUrl):
    wbc = crawling(username,password,targetUser)
    if len(targetUrl)> 0:
        print("album url is specified; goes directly to it")
        wbc.driver.get(targetUrl)
    else:
        wbc.getAlbumPage()

    html = wbc.driver.page_source
    print("--------begin to download--------")
    imageDL = downloading(html)

    # downloading from virtual machine could be pretty slow,
    # thus one can copy all the links` url and download the images on windows
    if onlyTxt is False:
        imageDL.getImages()
    else:
        print("links are stored")

if __name__ == '__main__':
    weiboCrawler(username,password,targetUser,targetUrl)
else:
    print("weibo.py cannot be exported to other module")
