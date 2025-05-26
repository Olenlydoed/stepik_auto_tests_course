import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    get_num1 = int(browser.find_element(By.ID, "num1").text)
    get_num2 = int(browser.find_element(By.ID, "num2").text)

    answer_list = Select(browser.find_element(By.ID, "dropdown"))
    answer_list.select_by_value(str(get_num1 + get_num2))

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
