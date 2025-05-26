import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
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


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
try:
    cost = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    button = browser.find_element(By.ID, "book")
    button.click()

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "solve")))
    x = int(browser.find_element(By.ID, "input_value").text)
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(calc(x))

    button = browser.find_element(By.ID, "solve")
    button.click()

    copy_accept_code_to_clipboard(browser)

except:
    time.sleep(10)
    browser.quit()
