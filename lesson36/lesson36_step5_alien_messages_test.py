import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from for_lesson36_step4 import email, sappword

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    #browser = webdriver.Firefox()
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('maybe_link', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_registration_on_stepik(browser, maybe_link):
    link = f"https://stepik.org/lesson/{maybe_link}/step/1/"
#def test_registration_on_stepik(browser):
    #link = "https://stepik.org/lesson/236905/step/1/"
    browser.get(link)
    time.sleep(5)
    button_cookie = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.woof-message__button'))).click()
    button_login = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button'))).click()
    input_email = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#id_login_email')))
    input_email.send_keys(email)
    
    input_password = browser.find_element(By.CSS_SELECTOR, '#id_login_password')
    input_password.send_keys(sappword)
    
    button = browser.find_element(By.CSS_SELECTOR, ".sign-form__btn")
    button.click()
    time.sleep(8)

    if len(browser.find_elements(By.XPATH, "//textarea[@disabled]")) > 0:
        button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.again-btn.white")))
        button.click()

        WebDriverWait(browser, 10).until_not(EC.presence_of_element_located((By.XPATH, "//textarea[@disabled]")))

    text_area = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.ember-text-area.ember-view.textarea.string-quiz__textarea')))
    
    answer = str(math.log(int(time.time())))
    text_area.send_keys(answer)
    button = browser.find_element(By.CSS_SELECTOR, '.submit-submission')
    button.click()
    time.sleep(5)

    element = WebDriverWait(browser, 10).until( EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")) )
    result = element.text
    if result != "Correct!":
        print(f"\033[31m\033[7;1m   {result}   \033[0m")
    assert result == "Correct!", f"Ожидался текст: \033[92;1m\033[7;1m 'Correct!'\033[0m, но получено: \033[31m\033[7;1m   {result}   \033[0m"    

