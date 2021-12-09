from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select

my_drv = webdriver.Chrome(executable_path="/home/modi/devops-experts/devops-experts/lesson_4/selenium/chromedriver")
my_drv.get('file:///home/modi/devops-experts/devops-experts/lesson_4/tip_calc/index.html')
print(my_drv.find_element_by_xpath("/html/body/div/div[1]/p[2]").text)
my_drv.close()


