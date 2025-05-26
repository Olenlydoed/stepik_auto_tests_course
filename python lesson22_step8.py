import os.path

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)


try:
    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("firstname")

    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("lastname")

    mail = browser.find_element(By.NAME, "email")
    mail.send_keys("mail")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file = "file.txt"
    file_path = os.path.join(current_dir, file)
    element_for_file = browser.find_element(By.ID, "file")
    # element_for_file.click()
    element_for_file.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

finally:
    time.sleep(10)
    browser.quit()