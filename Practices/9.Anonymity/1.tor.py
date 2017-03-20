from selenium import webdriver
import requests

# use Selenium and PhantomJS with Tor
# Tor service is running on port 9150 
service_args = [ '--proxy=localhost:9150', '--proxy-type=socks5', ]
driver = webdriver.PhantomJS(executable_path='../8.avoidTrap/phantomjs', \
                             service_args=service_args)
driver.get("http://icanhazip.com")
print(driver.page_source)
driver.close()
