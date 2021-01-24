from selenium import webdriver
from utilities.startup import open_site
from config import base_url
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver import ActionChains
import requests

browser = open_site(base_url)
assert "The Internet" in browser.title

slider = browser.find_element_by_xpath('//*[text()="Horizontal Slider"]').click()
slider2 = browser.find_element_by_xpath('//input[@type="range"]').click()
#assert range == 5

#targetEle = browser.find_element_by_id("range")
#targetEleXOffset = targetEle.location.get("x")
#targetEleYOffset = targetEle.location.get("y")
#webdriver.ActionChains.drag_and_drop_by_offset(browser, slider2, targetEleXOffset, targetEleYOffset).perform()

browser.back()

img = browser.find_element_by_xpath('//a[text()="Broken Images"]').click()
images = browser.find_elements_by_css_selector("img")

for image in images:
    print(image.get_attribute("src"))
    findimg = requests.get(image.get_attribute("src"))
    print(findimg.status_code)
    if findimg.status_code != 200:
        print(image.get_attribute("src"), "The image is broken!")

browser.back()

con = browser.find_element_by_xpath('//a[text()="Context Menu"]').click()
source = browser.find_element_by_id("hot-spot")
action = ActionChains(browser)
action.context_click(source).perform()

browser.switch_to_alert().accept()

browser.back()

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

checkbox = browser.find_element_by_xpath('//a[text()="Forgot Password"]').click()
email = browser.find_element_by_id('email')
email.send_keys('test@data.gr')

retrieve_button = browser.find_element_by_xpath('//i[contains(text(),"Retrieve password")]').click()

browser.back()
browser.back()

inputs1 = browser.find_element_by_xpath('//a[text()="Inputs"]').click()
inputs2 = browser.find_element_by_xpath('//input')
inputs2.send_keys('123456789')

assert inputs2.get_attribute('value') == '123456789'

browser.back()

checkbox = browser.find_element_by_xpath('//a[text()="Add/Remove Elements"]').click()
add = browser.find_element_by_xpath('//button[text()="Add Element"]').click()
delete = browser.find_element_by_xpath('//button[text()="Delete"]').click()
browser.back()

authedication = browser.find_element_by_xpath('//a[text()="Basic Auth"]').click()
browser.current_window_handle
browser.window_handles
browser.switch_to_window('basic auth')
browser.send_keys('admin')







