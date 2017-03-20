from urllib.request import urlopen
from bs4 import BeautifulSoup
from bs4 import re
import string

def clean(input):
    input = re.sub('\n+'," ",input)  # eliminate the newline character
    input = re.sub('\[[0-9]*\]',"",input)   # eliminate numbers
    input = re.sub(' +'," ",input)   # eliminate multiple spaces in a row
    input = bytes(input,'utf-8')     # eliminate escapse characters
    input = input.decode('ascii','ignore')
    cleanInput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)  # eliminate punctuation characters
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput


def getnGrams(input,n):
    input = clean(input)
    output = []
    for i in range(len(input)-n+1):
        output.append(input[i:i+n])
    return output

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html,"lxml")
content = bsObj.find("div", {"id":"mw-content-text"}).get_text()

nGrams = getnGrams(content,2)
print(ngrams)
print("length is " + str(len(ngrams)))
