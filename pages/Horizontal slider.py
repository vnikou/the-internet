from selenium import webdriver
from utilities.startup import open_site
from config import base_url
 
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
