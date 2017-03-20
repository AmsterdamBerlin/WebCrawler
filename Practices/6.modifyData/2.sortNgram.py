from urllib.request import urlopen
from bs4 import BeautifulSoup
from bs4 import re
import string
import operator

def isCommon(ngram):
    commonWords = ["the", "be", "and", "of", "a", "in", "to", "have", "it", "i", "that", "for", "you", "he", "with", "on", "do", "say", "this", "they", "is", "an", "at", "but","we", "his", "from", "that", "not", "by", "she", "or", "as", "what", "go", "their","can", "who", "get", "if", "would", "her", "all", "my", "make", "about", "know", "will","as", "up", "one", "time", "has", "been", "there", "year", "so", "think", "when", "which", "them", "some", "me", "people", "take", "out", "into", "just", "see", "him", "your", "come", "could", "now", "than", "like", "other", "how", "then", "its", "our", "two", "more", "these", "want", "way", "look", "first", "also", "new", "because", "day", "more", "use", "no", "man", "find", "here", "thing", "give", "many", "well"]
    for word in ngram:
        if word in commonWords:
            return True
    return False

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


def getNgrams(input,n):
    input = clean(input)
    output = {}
    for i in range(len(input)-n+1):
        NgramTemp = " ".join(input[i:i+n])
        if isCommon(NgramTemp.split(' ')) is True:  # get ride of common words
            continue

        if NgramTemp not in output:
            output[NgramTemp] = 0
        output[NgramTemp] += 1
    return output


#@ Ngram temp is: station according
#= it is common words: station according
#----------------------------
#@ Ngram temp is: according to
#= it is common words: according to


content = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").\
            read(),'utf-8')
Ngrams = getNgrams(content, 2)
sortedNgrams = sorted(Ngrams.items(), key = operator.itemgetter(1), reverse=True)

print(sortedNgrams[:5])
print("length is " + str(len(sortedNgrams)))
