from utilities.startup import open_site
from config import base_url

browser = open_site(base_url)
assert "The Internet" in browser.title

checkbox = browser.find_element_by_xpath('//a[text()="Forgot Password"]').click()
email = browser.find_element_by_id('email')
email.send_keys('test@data.gr')

retrieve_button = browser.find_element_by_xpath('//i[contains(text(),"Retrieve password")]').click()

browser.back()
