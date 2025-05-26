from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import pyperclip


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

def copy_accept_code_to_clipboard(driver: webdriver) -> None:
    alert = driver.switch_to.alert
    alert_text = alert.text
    accept_code = alert_text.split(':')[-1].strip()
    pyperclip.copy(accept_code)  # Копируем текст в буфер обмена
    print(f'Код скопирован в буфер обмена: {accept_code}')  # Уведомление


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)


try:
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = int(browser.find_element(By.ID, "input_value").text)
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(calc(x))

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

    copy_accept_code_to_clipboard(browser)

finally:
    time.sleep(10)
    browser.quit()
