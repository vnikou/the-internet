def open_site(base_url):

    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(ChromeDriverManager().install())

    browser = webdriver.Chrome()
    browser.get(base_url)
    browser.maximize_window()
    return browser
