from selenium import webdriver
from utilities.startup import open_site
from config import base_url
from selenium.webdriver.common.keys import Keys

browser = open_site(base_url)
assert "The Internet" in browser.title

inputs1 = browser.find_element_by_xpath('//a[text()="Inputs"]').click()
inputs2 = browser.find_element_by_xpath('//input')
inputs2.send_keys('123456789')

assert inputs2.get_attribute('value') == '123456789'

browser.back()
