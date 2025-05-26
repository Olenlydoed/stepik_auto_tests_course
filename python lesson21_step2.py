import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)

x_field = browser.find_element(By.CSS_SELECTOR, ".form-control")
x_field.send_keys(y)

checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
checkbox.click()

radiobtn = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
radiobtn.click()

button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
button.click()

time.sleep(10)
