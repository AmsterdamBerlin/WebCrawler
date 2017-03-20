import requests

# login data is stored in cookies
params = {'username': 'Starfucker','password': 'password'}
req = requests.post("http://pythonscraping.com/pages/cookies/welcome.php", data = params) 
print(req.text)
print("Cookie is set to:")
print(req.cookies.get_dict())
print("-----------")
print("Going to profile page…")
req = requests.get("http://pythonscraping.com/pages/cookies/profile.php", cookies=req.cookies)

print(req.text)
