from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class RegistrationSuccessfull(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
    
        input1 = browser.find_element(By.CSS_SELECTOR, "input.first[required]")
        input1.send_keys("Joseph")
        input2 = browser.find_element(By.CSS_SELECTOR, "input.second[required]")
        input2.send_keys("Bloggs")
        input3 = browser.find_element(By.CSS_SELECTOR, "input.third[required]")
        input3.send_keys("josephbloggs035@gmail.com")
    
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
    
        # ждем загрузки страницы
        time.sleep(1)
    
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        
        self.assertEqual('Congratulations! You have successfully registered!', welcome_text) 
    
        browser.quit()

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
    
        input1 = browser.find_element(By.CSS_SELECTOR, "input.first[required]")
        input1.send_keys("Joseph")
        input2 = browser.find_element(By.CSS_SELECTOR, "input.second[required]")
        input2.send_keys("Bloggs")
        input3 = browser.find_element(By.CSS_SELECTOR, "input.third[required]")
        input3.send_keys("josephbloggs035@gmail.com")
    
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
    
        # ждем загрузки страницы
        time.sleep(1)
    
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        
        self.assertEqual('Congratulations! You have successfully registered!', welcome_text) 
    
        browser.quit()

if __name__ == '__main__':
    unittest.main()
