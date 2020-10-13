from utilities.startup import open_site
from config import base_url
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver import ActionChains

import time

browser = open_site(base_url)

assert "The Internet" in browser.title

con = browser.find_element_by_xpath('//a[text()="Context Menu"]').click()
source = browser.find_element_by_id("hot-spot")
action = ActionChains(browser)
action.context_click(source).perform()
obj = browser.switch_to.alert
obj.accept()


button = browser.find_element_by_name("alert").click()
#Switch the control to the Alert window

print(" Clicked on the OK Button in the Alert Window")

browser.back()


img = browser.find_element_by_xpath('//a[text()="Broken Images"]').click()
images = browser.find_elements_by_tag_name('img')
images.__getattribute__('src')

if images.getattribute("src"):
    print("dsdsd")
assert isinstance(images.getattribute, 'asdf.jpg')



browser.back()

authedication = browser.find_element_by_xpath('//a[text()="Basic Auth"]').click()
alert  = browser.switch_to_alert()
alert.send_keys('admin')

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









