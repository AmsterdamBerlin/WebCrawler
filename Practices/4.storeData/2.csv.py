import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

def getNumberCsv():
    csvFile = open("test.csv","wt")
    try:
        writer = csv.writer(csvFile)
        writer.writerow(('number','number + 2','number * 2'))
        for i in range(10):
            writer.writerow((i,i+2,i*2))
    finally:
        csvFile.close()
        return 1

html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html,"lxml")

csvFile = open("editor.csv","wt")
writer = csv.writer(csvFile)
table = bsObj.findAll("table",{"class":"wikitable"})[0]
print(table.get_text())
print("______________________________")
rows = table.findAll("tr")

try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td','th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()
