import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--no-sandbox")
chromeOptions.add_argument("--disable-dev-shm-using")
chromeOptions.add_argument("--disable-extensions")
# chromeOptions.add_argument(r"user-data-dir=.\cookies\\test")
chromeOptions.headless = True
# If you have Chromedriver In Same folder then you dont need to pass executable path...
# driver = webdriver.Chrome(chrome_options=chromeOptions)
driver = webdriver.Chrome(executable_path="/home/modi/dev/devops-experts/lesson_4/selenium/chromedriver")

driver.get('https://www.google.com')

# Sometimes Google Duplicates That Input Field So we have to iterate...

inputElems = driver.find_elements(by=By.CSS_SELECTOR, value='input[name=q]')

print(inputElems)
for inputElem in inputElems:
    inputElem.send_keys('Modi Tamam')

    # Presses Enter Key Like When You Press Enter Key to Search
    inputElem.send_keys(Keys.ENTER);
    weblinks = driver.find_elements(by=By.XPATH, value="//div[@class='g']//a[not(@class)]");
    for element in weblinks:
        link = element.get_attribute("href")
        if 'linkedin' in link:
            print(link)
            break

driver.get('https://www.linkedin.com/')
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
wait = WebDriverWait(driver, 10)
wait.until(EC.title_contains('Log'))

# Login username/password
email_box = driver.find_element(by=By.ID, value='session_key')
email_box.send_keys('XXX')
pass_box = driver.find_element(by=By.ID, value='session_password')
pass_box.send_keys('XXX')
submit_button = driver.find_element(by=By.CLASS_NAME, value='sign-in-form__submit-button')
submit_button.click()


driver.get(link)
time.sleep(5)
print(driver.find_element(by=By.XPATH, value='//*[@id="ember45"]/div[2]/div[2]/div[1]/div[2]').text)
driver.close()
