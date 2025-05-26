import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)

chest = browser.find_element(By.ID, "treasure")
get_value = chest.get_attribute("valuex")
y = calc(get_value)

x_field = browser.find_element(By.ID, "answer")
x_field.send_keys(y)

checkbox = browser.find_element(By.ID, "robotCheckbox")
checkbox.click()

radiobtn = browser.find_element(By.ID, "robotsRule")
radiobtn.click()

button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
button.click()

time.sleep(10)
