from bs4 import BeautifulSoup
from collections import namedtuple
import requests
import binascii
import base64
import json
import rsa
import re
import os

login_url = "https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)"
pre_url = "https://login.sina.com.cn/sso/prelogin.php?entry=sso&callback=sinaSSOController.preloginCallBack&su=YXNk&rsakt=mod&client=ssologin.js(v1.4.15)"



class client:
    def __init__(self,username=None,password=None):
        self.username = username
        self.password = password
        self.nickname = None
        self.uid = None
        self.session = None
        self.album_info = None

    def __prelogin(self):
        req = requests.get(pre_url)
        jsonStr = re.findall('\((\{.*?\})\)', req.text)[0]
        data = json.loads(jsonStr)
        servertime = data['servertime']
        pcid       = data['pcid']
        nonce      = data['nonce']
        pubkey     = data['pubkey']
        rsakv      = data['rsakv']

        return servertime, nonce, pubkey, rsakv

    def __getSu(self, username):
        # encrypt username into su
        self.username = username
        su = base64.b64encode(username.encode('utf-8')).decode('utf-8')
        return su

    def __getSp(self, password,servertime, nonce, pubkey):
        self.password = password
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

    def __organize(self,su,sp,servertime, nonce, pubkey, rsakv):
        post_data = {
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

        return headers, post_data

    def __redirect(self, response):
        info = response.json()
        #print(info)
        link_1 = info["crossDomainUrlList"][0]
        link_2 = info["crossDomainUrlList"][1]
        self.nickname = info["nick"]
        self.uid = info["uid"]
        # weibo login is so annoying that it requires two more redirecting to get needed cookies/info
        redirect_1 = self.session.get(link_1)
        redirect_2 = self.session.get(link_2)

        if redirect_2.json()['retcode'] == 20000000:
            return True
        else:
            return False


    def login(self, username, password): #su, sp, servertime, nonce, rsakv
        servertime, nonce, pubkey, rsakv = self.__prelogin()
        su = self.__getSu(username)
        sp = self.__getSp(password,servertime, nonce, pubkey)
        headers, post_data = self.__organize(su,sp,servertime, nonce, pubkey, rsakv)

        self.session = requests.session()
        self.session.headers.update(headers)
        res = self.session.post(login_url, data=post_data)

        rd_success = self.__redirect(res)

        if rd_success == True:
            print("login success: \n", "nickname is: ", self.nickname, "user ID is: ", self.uid)
        else:
            print("login failes")

        return self.session

    def __find_albums(self):
        album_url = "http://photo.weibo.com/albums/get_all"
        info_album = namedtuple("info_album", "name, id, size, type")
        params_album = {
            'uid': self.target_uid,
            'page': '1',
            'count': '20',
        }

        info = self.session.get(album_url, params = params_album).json()['data']
        album_list = info['album_list']
        # sort the album out of the info; a struct is needed to store those data
        album_info = [info_album(name=album['caption'],
                                 id=album['album_id'],
                                 size=album['count']['photos'],
                                 type=album['type'])
                      for album in album_list]
        for album in album_info:
            print(album)
        return album_info

    def __find_photos(self,album, count, page):
        info_photo = namedtuple('info_photo', "photo_url, photo_id")
        photo_url = "http://photo.weibo.com/photos/get_all"
        params_photo = {
            'uid': self.target_uid,
            'album_id': album.id,
            'count': count,
            'page': page,
            'type': album.type,
        }
        info_album = self.session.get(photo_url,params = params_photo).json()['data']
        print(params_photo)
        photo_list = info_album['photo_list']
        #work = self.write_url(photo_url, album)
        photo_url =[]
        for photo in photo_list:
            photo_url.append(photo['pic_host'] + '/large/' + photo['pic_name'] + '\n')

        print('-------')
        return photo_url

    def __write_url(self,photo_url, album, index):
        path = "./url/" + album.name
        txt = str(index) + "_url.txt"
        txt_path = os.path.join(path, txt)
        if not os.path.exists(path):
            os.makedirs(path)
        # ---- collect urls of images that are going to be downloaded
        with open(txt_path,'w') as f:
            f.write(''.join(photo_url))
        print("links are stored")

    def __write_pic(self,photo_url, album, index):
        path = "./pic/" + album.name
        jpg_path = os.path.join(path)
        if not os.path.exists(path):
            os.makedirs(path)
        # ---- collect urls of images that are going to be downloaded
        for i, url in  enumerate(photo_url):
            response = self.session.get(url)
            pic = response.content
            with open(os.path.join(path, str(index)+'_'+str(i)+".jpg"),"wb") as f:
                f.write(pic)
        print("images are stored")

    def __collect_album(self,album):
        pic_num = 50
        page_num = int(album.size/pic_num) + 1
        for page_iter in range(page_num):
            photo_url = self.__find_photos(album,pic_num,page_iter+1)
            self.__write_url(photo_url, album, page_iter+1)
            self.__write_pic(photo_url, album, page_iter+1)
            print(page_iter, '\n', album.name)


    def download(self, target_uid):
        self.target_uid = target_uid
        self.album_info = self.__find_albums()

        for album in self.album_info:
            if album.size > 0:
                self.__collect_album(album)

        self.session.close()


        # write down urls
