from selenium import webdriver
from utilities.startup import open_site
from config import base_url
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException

browser = open_site(base_url)
assert "The Internet" in browser.title

authentication = browser.find_element_by_xpath('//a[text()="Basic Auth"]').click()
time.sleep(10)
#alert = browser.switch_to_alert()
#ActionChains(browser).send_keys('admin')
#ActionChains(browser).send_keys(Keys.TAB).perform()
#ActionChains(browser).send_keys('admin')
browser.switch_to.alert.accept()
browser.switch_to.alert.send_keys('123456' + Keys.TAB + '123456')

browser.back()
