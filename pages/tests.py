from selenium import webdriver
from utilities.startup import open_site
from config import base_url
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time
import requests

browser = open_site(base_url)
assert "The Internet" in browser.title

# checkboxes page
checkbox = browser.find_element_by_xpath('//a[text()="Checkboxes"]').click()


checkbox2 = browser.find_element_by_xpath('//input[@type="checkbox"][2]')

if checkbox2.is_selected() == False:
    checkbox2.click()

checkbox1 = browser.find_element_by_xpath('//input[@type="checkbox"][1]')

if checkbox1.is_selected() == False:
    checkbox1.click()

assert checkbox1.get_attribute('checked')

browser.back()

#Check broken images

img = browser.find_element_by_xpath('//a[text()="Broken Images"]').click()
images = browser.find_elements_by_css_selector("img")

for image in images:
    print(image.get_attribute("src"))
    findimg = requests.get(image.get_attribute("src"))
    print(findimg.status_code)
    if findimg.status_code != 200:
        print(image.get_attribute("src"), "The image is broken!")

browser.back()
authentication = browser.find_element_by_xpath('//a[text()="Basic Auth"]').click()
time.sleep(10)
#alert = browser.switch_to_alert()
#ActionChains(browser).send_keys('admin')
#ActionChains(browser).send_keys(Keys.TAB).perform()
#ActionChains(browser).send_keys('admin')
browser.switch_to.alert.send_keys('123456' + Keys.TAB + '123456')

browser.switch_to.alert.accept()

browser.back()

con = browser.find_element_by_xpath('//a[text()="Context Menu"]').click()
source = browser.find_element_by_id("hot-spot")
action = ActionChains(browser)
action.context_click(source).perform()

browser.switch_to_alert().accept()
print("alert accepted")

browser.back()

#Input

inputs1 = browser.find_element_by_xpath('//a[text()="Inputs"]').click()
inputs2 = browser.find_element_by_xpath('//input')
inputs2.send_keys('123456789')

assert inputs2.get_attribute('value') == '123456789'

browser.back()
#Add/remove elements

checkbox = browser.find_element_by_xpath('//a[text()="Add/Remove Elements"]').click()
add = browser.find_element_by_xpath('//button[text()="Add Element"]').click()
delete = browser.find_element_by_xpath('//button[text()="Delete"]').click()
browser.back()

#Horizontal slider

slider = browser.find_element_by_xpath('//*[text()="Horizontal Slider"]').click()
slider2 = browser.find_element_by_xpath('//input[@type="range"]').click()
#assert range == 5

#targetEle = browser.find_element_by_id("range")
#targetEleXOffset = targetEle.location.get("x")
#targetEleYOffset = targetEle.location.get("y")
#webdriver.ActionChains.drag_and_drop_by_offset(browser, slider2, targetEleXOffset, targetEleYOffset).perform()

browser.back()

#Forgot password

checkbox = browser.find_element_by_xpath('//a[text()="Forgot Password"]').click()
email = browser.find_element_by_id('email')
email.send_keys('test@data.gr')

retrieve_button = browser.find_element_by_xpath('//i[contains(text(),"Retrieve password")]').click()

browser.back()






