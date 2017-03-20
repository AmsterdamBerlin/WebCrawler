from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html,"lxml")

# filtering with more condition
headlist = bsObj.findAll({"h1","h2","h3","h4","h5","h6"})
for head in headlist:
    print(head.get_text())

namelist = bsObj.findAll("span",{"class":"read", "class":"green"})
for name in namelist:
    print(name.get_text())


#########   use key work argument
princelist = bsObj.findAll(text = "the prince")
print(len(princelist))

text = bsObj.findAll(id = "text")
#  text = bsObj.findAll("",{"id","text"})
print( len(text))

redClass0 = bsObj.findAll("span",{"class":"red"})
redClass1 = bsObj.findAll(class_ = "red")
redClass2 = bsObj.findAll("",{"class":"red"})

print(len(redClass0) )
print(len(redClass1) )
print(len(redClass2) )
