from bs4 import BeautifulSoup
from login import client
import time




if __name__ == "__main__":
    weibo_client = client()
    session = weibo_client.login(username,password)
    #targetUrl = "http://photo.weibo.com/"+targetUid
    # res = session.get(targetUrl)
    # info = res.content.decode('utf-8','ignore')
    # print(info)
    params = {
        'uid': targetUid,
        'page': 1,
        'count': 20
    }
    albumUrl = "http://photo.weibo.com/albums/get_all?"
    photoUrl = "http://photo.weibo.com/photos/get_all?"
    info = session.get(albumUrl).json()['data']
    print(info['total'])
    album_list = info["album_list"]
    album_1 = album_list[1]
    params_1 = {
        'uid': targetUid,
        'album_id': album_id,
        'count': 30,
        'page': 1,
        #'type': 18
    }
    print(album_1["caption"])
    info_album = session.get(photoUrl,params = params_1).json()['data']
    photo_list = info_album
    print(photo_list)

    session.close()
