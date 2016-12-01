# coding : utf-8
from selenium import webdriver
import time
browser =webdriver.Chrome()
browser.get('https://www.baidu.com')

print "max window"
browser.maximize_window() 
time.sleep(2)
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click

time.sleep(5)
browser.quit()