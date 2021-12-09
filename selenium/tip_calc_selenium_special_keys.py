from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(executable_path="/home/modi/dev/devops-experts/lesson_4/selenium/chromedriver")
browser.get('file:///home/modi/dev/devops-experts/lesson_4/tip_calc/index.html')
sleep(1)
browser.find_element(by=By.ID, value='billamt').send_keys("100" + Keys.TAB + Keys.DOWN + Keys.DOWN + Keys.ENTER)

# get selected value:
select = Select(browser.find_element(by=By.ID, value='serviceQual'))
selected_option = select.first_selected_option
print (selected_option.text)

# select by visible text
browser.find_element(by=By.ID, value="music-quality").send_keys("4")
browser.find_element(by=By.ID, value="peopleamt").send_keys("4")
browser.find_element(by=By.ID, value="calculate").click()
actual = browser.find_element(by=By.ID, value="tip").text
print("actual: {0}".format(actual))
expected = "11.50"
try:
    assert actual == expected, "Error"
    sleep(2)
finally:
    browser.close()