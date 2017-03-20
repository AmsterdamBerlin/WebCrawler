import json
from urllib.request import urlopen

# get a specific info. item from the info. list, e.g., city, country_name, zip_code, etc.
def getCountry(ipAddress):
    response = urlopen("http://freegeoip.net/json/"
                       + ipAddress).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get("city")

print(getCountry("50.78.253.58"))



# translate JSON objects to python objects
jsonString = '{"arrayOfNums":[{"number":0},{"number":1},{"number":2}],\
              "arrayOfFruits":[{"fruit":"apple"},{"fruit":"banana"},{"fruit":"pear"}]}'
jsonObj = json.loads(jsonString)

print(jsonObj.get("arrayOfNums"))
print(jsonObj.get("arrayOfNums")[1])
print(jsonObj.get("arrayOfNums")[1].get("number") + jsonObj.get("arrayOfNums")[2].get("number"))
print("__________________________________\n")
print(jsonObj.get("arrayOfFruits"))
print(jsonObj.get("arrayOfFruits")[2])
print(jsonObj.get("arrayOfFruits")[2].get("fruit"))
