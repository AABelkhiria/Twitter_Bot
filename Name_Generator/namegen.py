from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
import os
import sys
from time import sleep
import csv
import random

def restart_program():
    print('Restarting Program')
    print('\n')
    python = sys.executable
    os.execl(python, python, * sys.argv)

def geturl(url):
    print('geturl()')
    try:
        print('Trying to get URL')
        browser.get(url)
        print('Page loaded : ',url)
        return 1
    except TimeoutException:
        print('Failed 1 : TimeoutException')
        return 0
    except WebDriverException:
        print('Failed 1 : WebDriverException')
        return 0

def chckelt(elem):
    print('chckelt()')
    global elt
    try:
        print('Checking existance of Sign up button')
        browser.find_element_by_xpath(elem)
        return 1
    except NoSuchElementException:
        print('Failed 2 : NoSuchElementException')
        return 0

# Main Program

print('Starting Firefox')
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.cache.disk.enable", False)
profile.set_preference("browser.cache.memory.enable", False)
profile.set_preference("browser.cache.offline.enable", False)
profile.set_preference("network.http.use-cache", False)
profile.set_preference("general.useragent.override", "Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0")
browser = webdriver.Firefox(profile)
print('Firefox Opened')

while (1):
    if (geturl('https://www.behindthename.com/random/random.php?number=1&gender=f&surname=&randomsurname=yes&all=no&usage_eng=1&usage_fre=1') ):
        pass
    else:
        if ( chckelt("//html/body/div/div/center/p/span") ):
            pass
        else :
            restart_program()

    name = browser.find_element_by_xpath("//html/body/div/div/center/p/span/a").get_attribute("text")
    sur = browser.find_elements_by_xpath("//html/body/div/div/center/p/span/a")[1].get_attribute("text")

    print('Name generated : ',name,' ',sur)
    
    f = open("name_sur.txt", "a")
    f.write(name)
    f.write(' ')
    f.write(sur)
    f.write("\n")
    f.close()

    print('\n')
