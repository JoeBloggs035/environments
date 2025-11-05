import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Firefox()
    browser.get("http://suninjuly.github.io/registration2.html")
    
    first_name_input = browser.find_element(By.CSS_SELECTOR, "div.first_block .form-control.first")
    first_name_input.send_keys("Ivan")

    last_name_input = browser.find_element(By.CSS_SELECTOR, "div.first_block .form-control.second")
    last_name_input.send_keys("Petrov")

    email_input = browser.find_element(By.CSS_SELECTOR, "div.first_block .form-control.third")
    email_input.send_keys("ivan.petrov@example.com")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
