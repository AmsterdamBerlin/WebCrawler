from urllib.request import urlopen
from bs4 import BeautifulSoup
import json


def getHistoryIPs(pageUrl):
    addressList = set()

    #Format of revision history pages is:
    #http://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history

    pageUrl = pageUrl.replace("/wiki/","")
    historyUrl = "http://en.wikipedia.org/w/index.php?title="\
                 +pageUrl + "&action=history"
    print("history URL is: " + historyUrl)

    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html,"lxml")

    ipAddresses = bsObj.findAll("a",{"class":"mw-anonuserlink"})
    for ip in ipAddresses:
        addressList.add(ip.get_text())
    return addressList

def getContry(ip):
    try:
        response = urlopen("http://freegeoip.net/json/"
                           + ip).read().decode('utf-8')
    except HTTPError:
        return None
    responseJson = json.loads(response)
    return responseJson.get("country_name")

# check the country of an ip address who edited the wiki page: python program
link = "/wiki/Python_(programming_language)"
IPs = getHistoryIPs(link)
if(len(IPs)):
    print("Link: http://en.wikipedia.org/" + link)
    for ip in IPs:
        country = getContry(ip)
        if country is not None:
            print("@" + ip + " is from: " + country )
