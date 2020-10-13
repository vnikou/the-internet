def open_site(base_url):


    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(ChromeDriverManager().install())

    from selenium.webdriver.common.alert import Alert

    browser = webdriver.Chrome('C:\\webdrivers\\chromedriver')
    browser.get(base_url)
    browser.maximize_window()
    return browser
