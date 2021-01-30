from selenium import webdriver
from utilities.startup import open_site
from config import base_url
import time
import requests

browser = open_site(base_url)
assert "The Internet" in browser.title

img = browser.find_element_by_xpath('//a[text()="Broken Images"]').click()
images = browser.find_elements_by_css_selector("img")

for image in images:
    print(image.get_attribute("src"))
    findimg = requests.get(image.get_attribute("src"))
    print(findimg.status_code)
    if findimg.status_code != 200:
        print(image.get_attribute("src"), "The image is broken!")

browser.back()
