import requests

# enter email address
params = {'firstname': 'Ryan', 'lastname': 'Mitchell'}
r1 = requests.post("http://pythonscraping.com/files/processing.php", data = params)
print(r1.text)

# upload an image
# files = {'uploadFile':open('./GkvBm1eg.jpg','rb')}
# r2 = requests.post("http://pythonscraping.com/pages/processing2.php",files=files)
#
# print(r2.text)
