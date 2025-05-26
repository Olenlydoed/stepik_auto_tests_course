from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
import os

# browser = webdriver.Chrome()
# browser.get(link)
# button = browser.find_element(By.TAG_NAME, "button")
# button.click()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)


try:
        # Поиск х и вставка в строку ввода
    get_num = int(browser.find_element(By.ID, "input_value").text)
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(calc(get_num))

    # Скролл страницы
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()

    radiobtn = browser.find_element(By.ID, "robotsRule")
    radiobtn.click()

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

finally:
    time.sleep(10)
    browser.quit()