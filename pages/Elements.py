from selenium import webdriver
from utilities.startup import open_site
from config import base_url
from time import sleep
import os

 
browser = open_site(base_url)
assert "The Internet" in browser.title


checkbox = browser.find_element_by_xpath('//a[text()="Add/Remove Elements"]').click()
sleep(0.5)

add = browser.find_element_by_xpath('//button[text()="Add Element"]').click()
sleep(0.5)

delete = browser.find_element_by_xpath('//button[text()="Delete"]')
#assert len(delete) == 1
delete.click()
sleep(0.5)

browser.back()
