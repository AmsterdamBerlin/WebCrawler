from bs4 import BeautifulSoup
import requests
import base64

baseUrl = "http://login.sina.com.cn/signup/signin.php?entry=sso"
searchUrl = "http://s.weibo.com"


username =   #"makeAmericaGreatAgain@qq.com"
password =          #"********"

def login(username, password):
    username = base64.b64encode(username.encode('utf-8')).decode('utf-8')
    postData = {
        "entry": "sso",
        "gateway": "1",
        "from": "null",
        "savestate": "30",
        "useticket": "0",
        "pagerefer": "",
        "vsnf": "1",
        "su": username,
        "service": "sso",
        "sp": password,
        "sr": "1440*900",
        "encoding": "UTF-8",
        "cdult": "3",
        "domain": "sina.com.cn",
        "prelt": "0",
        "returntype": "TEXT",
    }
    loginURL = r'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)'
    session = requests.Session()
    res = session.post(loginURL, data = postData)
    info = res.json()
    if info["retcode"] == "0":
        print("登录成功")
        print(info)
        # 把cookies添加到headers中，必须写这一步，否则后面调用API失败
        cookies = session.cookies.get_dict()
        cookies = [key + "=" + value for key, value in cookies.items()]
        cookies = "; ".join(cookies)
        session.headers["cookie"] = cookies
    else:
        print("登录失败，原因： %s" % info["reason"])
    return session

if __name__ == '__main__':
    session = login(username, password)
