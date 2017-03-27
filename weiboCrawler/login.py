from bs4 import BeautifulSoup
import requests
import binascii
import base64
import json
import rsa
import re

loginURL = "https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)"
preUrl = "https://login.sina.com.cn/sso/prelogin.php?entry=sso&callback=sinaSSOController.preloginCallBack&su=YXNk&rsakt=mod&client=ssologin.js(v1.4.15)"


def prelogin():
    req = requests.get(preUrl)
    jsonStr = re.findall('\((\{.*?\})\)', req.text)[0]
    data = json.loads(jsonStr)
    servertime = data['servertime']
    pcid       = data['pcid']
    nonce      = data['nonce']
    pubkey     = data['pubkey']
    rsakv      = data['rsakv']

    return servertime, nonce, pubkey, rsakv

def getSu( username):
    # encrypt username into su
    su = base64.b64encode(username.encode('utf-8')).decode('utf-8')
    return su

def getSp(password,servertime, nonce, pubkey):
    # encrypt password into sp
    # I don`t understand the procedure neither
    pubkey = int(pubkey, 16)
    # 65537是js加密文件文件中的固定值，原是十六进制数字10001
    key = rsa.PublicKey(pubkey, 65537)
    # 以下拼接明文从js加密文件中得到
    message = str(servertime) + '\t' + str(nonce) + '\n' + str(password)
    message = message.encode('utf-8')
    sp = rsa.encrypt(message, key)
    # 把二进制数据的每个字节转换成相应的2位十六进制表示形式。
    sp = binascii.b2a_hex(sp)
    return sp

def login(su, sp, servertime, nonce, rsakv):
    postData = {
        'entry': 'sso',
        'gateway': '1',
        'from': 'null',
        'savestate': '30',
        'userticket': '0',
        "pagerefer": "",
        "vsnf": "1",
        "su": su,
        "service": "sso",
        "servertime": servertime,
        "nonce": nonce,
        "pwencode": "rsa2",
        "rsakv": rsakv,
        "sp": sp,
        "sr": "1440*900",
        "encoding": "UTF-8",
        "cdult": "3",
        "domain": "sina.comc.cn",
        "prelt": "408",
        "returntype": "TEXT",
    }
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'
    }
    session = requests.session()
    #session.headers = headers
    session.headers.update(headers)
    res_post = session.post(loginURL, data=postData)
    info = res_post.json()
    #print(info)
    link_1 = info["crossDomainUrlList"][0]
    link_2 = info["crossDomainUrlList"][1]
    nickname = info["nick"]
    uid = info["uid"]
    print("link 1 is : ", link_1, "\n", "lind 2 is : ",link_2,"\n",nickname,'\n',uid)
    # weibo login is so annoying that it requires two more redirecting to get needed cookies/info
    redirect_1 = session.get(link_1)
    redirect_2 = session.get(link_2)

    if redirect_2.json()['retcode'] == 20000000:
        print("login success")
        res_get = session.get(targetUrl)
        print(res_get.headers)
    else:
        print("login failes")

    return session

if __name__ == "__main__":
    servertime, nonce, pubkey, rsakv = prelogin()
    su = getSu(username)
    sp = getSp(password,servertime, nonce, pubkey)
    session = login(su, sp, servertime, nonce, rsakv)
    res = session.get(targetUrl)
    #print(res.headers)
    #print(res.cookies)
    html = res.content
    #print(html)
    bsObj = BeautifulSoup(html,"lxml")

    #downloadList = bsObj.findAll("img",{"src":re.compile("http://ww")})
    #if len(downloadList) > 1:
    #    print("ncie")
