from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
import os
import sys
from time import sleep
import random

def restart_program():
    print('Restarting Program')
    python = sys.executable
    os.execl(python, python, * sys.argv)

def geturl(browser,url):
    print('geturl()')
    try:
        print('Trying to get URL : ',url)
        browser.get(url)
        print('Page loaded')
        return 1
    except TimeoutException:
        print('Failed 1 : TimeoutException')
        return 0
    except WebDriverException:
        print('Failed 1 : WebDriverException')
        return 0

def init(ver):
    print('Starting Firefox')
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.cache.disk.enable", False)
    profile.set_preference("browser.cache.memory.enable", False)
    profile.set_preference("browser.cache.offline.enable", False)
    profile.set_preference("network.http.use-cache", False)
    if ver == "mobile":
        profile.set_preference("general.useragent.override", "Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0")
    return webdriver.Firefox(profile)

def waitelem(browser,xpath):
    sleep(1)
    pas = 0
    while(1):
        try:
            browser.find_element_by_xpath(xpath)
            pas = 1
        except:
            print(' Error : Element not found')
            sleep(2)
        if pas == 1:
            break
            
def fillform(browser,xpath,obj):
    while(1):
        pas = 0
        try:
            champ = browser.find_element_by_xpath(xpath)
            champ.send_keys(obj)
            pas = 1
        except:
            sleep(1)
        if pas == 1:
            break

def clickelem(browser,xpath,verif):
    if verif == "verif":
        while(1):
            pas = 0
            try:
                browser.find_element_by_xpath(xpath)
                pas = 1
            except:
                sleep(1)
            if pas == 1:
                break

        browser.find_element_by_xpath(xpath).click()
    else:
        try:
            browser.find_element_by_xpath(xpath).click()
        except:
            print(" Element not fount in clicking on ",xpath)

def connect(mail,ver):
    browser = init(ver)
    geturl(browser,'https://mobile.twitter.com/login')

    sleep(2)

    print('Filling Mail form')
    fillform(browser,"/html/body/div/div/main/div/div/form/div/div[1]/div/input",mail)

    sleep(2)

    print('Filling Password form')
    fillform(browser,"/html/body/div/div/main/div/div/form/div/div[2]/div/input","21074000")

    sleep(2)

    print('Logging in')
    clickelem(browser,"/html/body/div/div/main/div/div/form/div/div[3]/div","verif")
    print('Connecting to ',mail)

    sleep(2)

    waitelem(browser,"/html/body/div/div[1]/header/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div")

    return browser
