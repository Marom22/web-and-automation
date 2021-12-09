from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(executable_path="/home/modi/dev/devops-experts/lesson_4/selenium/chromedriver")
browser.get('file:///home/modi/dev/devops-experts/lesson_4/tip_calc/index.html')
sleep(1)
browser.find_element(by=By.ID, value='billamt').send_keys("100")
sleep(1)
select = Select(browser.find_element(by=By.ID, value='serviceQual'))
sleep(1)

# select by visible text
select.select_by_value('0.3')
sleep(1)
browser.find_element(by=By.ID, value="music-quality").send_keys("4")
sleep(1)
browser.find_element(by=By.ID, value="peopleamt").send_keys("4")
sleep(1)
browser.find_element(by=By.ID, value="calculate").click()
sleep(1)
actual = browser.find_element(by=By.ID, value="tip").text
print("actual: {0}".format(actual))
expected = "11.50"
assert actual == expected, "Error"
sleep(2)
browser.close()