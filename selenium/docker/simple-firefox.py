import logging
from selenium import webdriver

logging.getLogger().setLevel(logging.INFO)
BASE_URL = 'http://www.google.com/'


def firefox_example():
    print("Using Firefox...")
    from selenium.webdriver.firefox.options import Options
    options = Options()
    options.add_argument("-headless")
    browser = webdriver.Firefox(options=options)
    browser.get(BASE_URL)
    print('Page title: ', browser.title)
    browser.quit()


if __name__ == '__main__':
    firefox_example()
