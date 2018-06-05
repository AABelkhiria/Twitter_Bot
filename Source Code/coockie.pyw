from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
import os
import sys
from time import sleep
import random


while 1:
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.cache.disk.enable", False)
    profile.set_preference("browser.cache.memory.enable", False)
    profile.set_preference("browser.cache.offline.enable", False)
    profile.set_preference("network.http.use-cache", False)

    a = webdriver.Firefox(profile)
    a.get("https://www.binance.com/?ref=19735913")
    
    a.execute_script("window.open('');")
    a.switch_to_window(a.window_handles[1])
    a.get('https://www.minuteinbox.com/')
    mail = a.find_element_by_id("email").get_attribute("innerHTML")

    a.switch_to_window(a.window_handles[0])

    a.find_element_by_xpath("/html/body/div[1]/div/div[2]/a[2]").click()
    sleep(5)

    a.find_element_by_xpath('//*[@id="email"]').send_keys(mail)
    sleep(1)

    a.find_element_by_xpath('//*[@id="regiterPassword"]').send_keys("Password1")
    sleep(1)

    a.find_element_by_xpath('//*[@id="regiterRepeatPassword"]').send_keys("Password1")
    sleep(1)

    a.find_element_by_xpath('//*[@id="agreement"]').click()
    sleep(1)

    a.find_element_by_xpath('//*[@id="register-btn"]').click()
    os.system("pause")

    a.switch_to_window(a.window_handles[1])
    sleep(15)

    a.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[2]/a').click()
    sleep(2)

    a.find_element_by_xpath("//tr[@data-href='2']").click()
    os.system("pause")

    a.quit()

    f = open("mails.txt", "a")
    f.write(mail)
    f.write("\n")
    f.close()
