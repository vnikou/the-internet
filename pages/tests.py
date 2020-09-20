from utilities.startup import open_site
from config import base_url
browser = open_site(base_url)

# checkboxes page
checkbox = browser.find_element_by_xpath('//a[text()="Checkboxes"]').click()

choice = browser.find_element_by_xpath('//input[@type="checkbox"][2]')

if choice.is_selected() == False:
    choice.click()

browser.back()
