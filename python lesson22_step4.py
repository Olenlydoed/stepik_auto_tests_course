import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.execute_script("document.title='Script executing';alert('Robots at work');")
    # browser.execute_script('document.title="Script executing";')
    # browser.execute_script("alert('Robots at work');")

finally:
    time.sleep(3)
    browser.quit()
