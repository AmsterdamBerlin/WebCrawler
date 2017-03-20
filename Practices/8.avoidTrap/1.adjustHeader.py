import requests
from bs4 import BeautifulSoup

#  Session object to manage and persist settings across requests (cookies, auth, proxies)
session = requests.Session()
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) \
            AppleWebKit 537.36 (KHTML, like Gecko) Chrome", \
            "Accept":"text/html,application/xhtml+xml,application/xml;\
            q=0.9,image/webp,*/*;q=0.8"}

# tips: use mobile agent may be easier for scraping
url = "https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending"
req = session.get(url, headers=headers)
print(req)
print("------------------------------")
bsObj = BeautifulSoup(req.text,"lxml")

print(bsObj.find("table",{"class":"table-striped"}).get_text)
