from selenium import webdriver

#  selenium is to automate web browser interaction from Python.

driver = webdriver.PhantomJS(executable_path='./phantomjs')
driver.get("http://pythonscraping.com")
driver.implicitly_wait(1)
print(driver.get_cookies())

savedCookies = driver.get_cookies()

driver2 = webdriver.PhantomJS(executable_path='./phantomjs')
driver2.get("http://pythonscraping.com")
driver2.implicitly_wait(1)

if driver.get_cookies() == driver2.get_cookies():
    print("true")
else:
    print("nope")

driver2.delete_all_cookies()

for cookie in savedCookies:
    # fix the 2nd problem
    for k in ('name', 'value', 'domain', 'path', 'expiry'):
        if k not in list(cookie.keys()):
            if k == 'expiry':
                cookie[k] = 1475825481
    # fix the 1st problem
    driver2.add_cookie({k: cookie[k] for k in ('name', 'value', 'domain', 'path', 'expiry') if k in cookie})
print(cookie)

driver2.get("http://pythonscraping.com")
driver2.implicitly_wait(1)
print(driver2.get_cookies())

if driver.get_cookies() == driver2.get_cookies():
    print("true")
else:
    print("nope")
