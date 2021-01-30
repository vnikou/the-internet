from selenium import webdriver
from utilities.startup import open_site
from config import base_url
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver import ActionChains

browser = open_site(base_url)
assert "The Internet" in browser.title

con = browser.find_element_by_xpath('//a[text()="Context Menu"]').click()
source = browser.find_element_by_id("hot-spot")
action = ActionChains(browser)
action.context_click(source).perform()

browser.switch_to_alert().accept()
print("alert accepted")

browser.back()
