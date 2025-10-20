from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    #element1 = browser.find_element(By.ID, "num1")
    x = int(browser.find_element(By.ID, "num1").text)
    element2 = browser.find_element(By.ID, "num2")
    y = int(element2.text)
    z = str(x + y)
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(z)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

