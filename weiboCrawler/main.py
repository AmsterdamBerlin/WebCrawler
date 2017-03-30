from bs4 import BeautifulSoup
from Pyclient import client
import time

username = 'makeAmericaGreatAgain@qq.com'
password = '********'         
target_uid = "666666666"


if __name__ == "__main__":
    weibo_client = client()
    session = weibo_client.login(username,password)
    weibo_client.download(target_uid)
