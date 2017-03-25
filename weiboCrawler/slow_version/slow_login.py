import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

baseUrl = "http://login.sina.com.cn/signup/signin.php?entry=sso"
searchUrl = "http://s.weibo.com"

class crawling():

    def __init__(self,username,password,targetUser):
        self.username = username
        self.password = password
        self.targetUser = targetUser
        self.driver = webdriver.PhantomJS(executable_path='../Practices/8.avoidTrap/phantomjs')
        self.driver.maximize_window()   # set a fake browser size before doing get

        #  ----  login  -----
        print("1 @ login weibo")
        self.driver.get(baseUrl)
        print(self.username)
        print(self.password)
        # clear content in username/password text box before write
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys(self.username)

        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys(self.password)

        self.driver.find_element_by_xpath("//input[@type='submit']").click()

        try:
            WebDriverWait(self.driver,10).until(EC.title_is("我的新浪_个人中心_新浪网"))
        except:
            print("login failed")
        else:
            print("login successed")


    def __search(self):
        print("2 @ search the user")
        self.driver.get(searchUrl)
        print("jump to the page" + self.driver.title)
        # clear the search box, input target user, and click search button
        #self.driver.find_element_by_xpath("//input[@class='searchInp_form']").clear()
        self.driver.find_element_by_xpath("//a[@action-data='type=user']").click()
        self.driver.find_element_by_xpath("//input[@class='searchInp_form']").send_keys(self.targetUser)
        self.driver.find_element_by_xpath("//a[@node-type='submit']").click()

        try:
            WebDriverWait(self.driver,10).until(EC.title_contains(self.targetUser))
        except:
            print("user NOT found!")
            print(self.driver.title)
        else:
            print("user found!")

    def __switch(self):
        print("3 @ switch to his/her main page")
        self.driver.find_element_by_xpath("//a[@suda-data='key=tblog_search_user&value=user_feed_1_name']").click()
        # after this click, two window handles are availabe.
        # the 1st one is current windows - search page; the 2nd one the the main page of the user - the one that we are going to
        self.mainpage = self.driver.window_handles[1]
        self.driver.switch_to_window(self.mainpage)

        # then navigate to the album window
        self.driver.find_element_by_xpath("//a[@suda-uatrack='key=tblog_profile_new&value=tab_photos']").click()
        # 3rd window is loaded, switch to it
        self.driver.find_element_by_xpath("//a[@suda-uatrack='key=v6_profilealbum&value=tab_album']").click()

        self.albumpage = self.driver.window_handles[2]
        self.driver.switch_to_window(self.albumpage)

        try:
            WebDriverWait(self.driver,10).until(EC.title_contains("微相册"))
        except:
            print("album page lost")
        else:
            print("album page loaded")


    def __album(self):
        print("4 @ specify which album to download -- here is profile album")
        # choose which album to download from the album page; here lets first locate profile album
        self.driver.find_element_by_xpath("//a[@title='头像相册']").click()
        try:
            WebDriverWait(self.driver,10).until(EC.title_contains("头像相册"))
        except:
            print("profile album lost")
        else:
            print("profile album loaded")

    def getAlbumPage(self):
        self.__search()
        print("-------------")
        self.__switch()
        print("-------------")
        self.__album()
