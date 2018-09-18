#!python3
# auto login qq email
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://mail.qq.com/cgi-bin/loginpage')
try:
    elemUsername = browser.find_element_by_xpath("//*[@id='u']")
    #elemUsername.send_keys('dliu320@qq.com')
    #elemPassword = browser.find_element_by_id('p')
    #elemPassword.send_keys('digimon7500566')
    #submitButton = browser.find_element_by_id('login_button')
    #submitButton.submit()
except:
    print('error')