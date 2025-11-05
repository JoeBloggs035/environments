from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

try:
    link = "https://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(15)
    if WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100')):
        button1=browser.find_element(By.ID, "book")
        button1.click()
    x_value=browser.find_element(By.ID, "input_value").text
    x=math.log(abs(12*math.sin(int(x_value))))
    input1=browser.find_element(By.ID, "answer")
    input1.send_keys(x)
    submit1=browser.find_element(By.ID, "solve")
    submit1.click()
    text=browser.switch_to.alert.text.split(" ")
    print(text[-1])
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    # закрываем браузер после всех манипуляций
    browser.quit()
