from utilities.startup import open_site
from config import base_url

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

checkbox = browser.find_element_by_xpath('//a[text()="Forgot Password"]').click()
email = browser.find_element_by_id('email')
email.send_keys('test@data.gr')

retrieve_button = browser.find_element_by_xpath('//i[contains(text(),"Retrieve password")]').click()

