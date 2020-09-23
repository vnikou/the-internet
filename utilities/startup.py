def open_site(base_url):


    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys

    browser = webdriver.Chrome('C:\\webdrivers\\chromedriver')
    browser.get(base_url)
    browser.maximize_window()
    return browser

 

