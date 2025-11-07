import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from for_lesson36_step4 import email, sappword

"""@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
"""
def test_registration_on_stepik(browser):
    link = "https://stepik.org/lesson/236895/step/1"
    browser.get(link)
    time.sleep(7)
    button = browser.find_element(By.CSS_SELECTOR, '.ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button')
    button.click()

    input_email = browser.find_element(By.CSS_SELECTOR, '#id_login_email')
    input_email.send_keys(email)
    
    input_password = browser.find_element(By.CSS_SELECTOR, '#id_login_password')
    input_password.send_keys(sappword)
    
    button = browser.find_element(By.CSS_SELECTOR, ".sign-form__btn")
    button.click()
    time.sleep(5)

    try:
        button = browser.find_element(By.CSS_SELECTOR, '.ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button')
        print("поп-ап авторизации все еще отображается")
    except NoSuchElementException:
        print("поп-апа с авторизацией больше нет")
#        time.sleep(10)


