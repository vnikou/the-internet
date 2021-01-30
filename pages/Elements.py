from selenium import webdriver
from utilities.startup import open_site
from config import base_url
 
browser = open_site(base_url)
assert "The Internet" in browser.title


checkbox = browser.find_element_by_xpath('//a[text()="Add/Remove Elements"]').click()
add = browser.find_element_by_xpath('//button[text()="Add Element"]').click()
delete = browser.find_element_by_xpath('//button[text()="Delete"]').click()
browser.back()
