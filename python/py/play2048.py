#!python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random

def randomPlay():
    r = random.randint(1, 4)
    if r == 1:
        return Keys.LEFT
    if r == 2:
        return Keys.UP
    if r == 3:
        return Keys.RIGHT
    return Keys.DOWN


browser = webdriver.Firefox()
#browser.get('https://gabrielecirulli.github.io/2048/')
browser.get('http://www.iplay2048.com')
try:
    #time.sleep(5)
    elem = browser.find_element_by_tag_name('html')
    #i = 0
    while (True):
        #time.sleep(1)
        try:
            browser.find_element_by_class_name('game-over')
            break
        except:
            elem.send_keys(randomPlay())
        
        #i += 1
except:
    print('over')