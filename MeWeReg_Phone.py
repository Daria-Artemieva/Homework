from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://master.ci.k8s.sgr-labs.com/"


def click():
    pass


try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.XPATH, '//span[@data-testid="reg-switch-phone"]')
    button.click()

    Name = browser.find_element(By.ID, 'reg-first-filled')
    Name.send_keys("Daria")
    time.sleep(0)
    Surname = browser.find_element(By.ID, 'reg-last-filled')
    Surname.send_keys("Test")
    time.sleep(1)
    Phone = browser.find_element(By.XPATH, '//input[@data-testid="phone-input"]').clear()
    time.sleep(3)
    Phone = browser.find_element(By.XPATH, '//input[@data-testid="phone-input"]')
    Phone.send_keys("89925863438")

    time.sleep(3)
    Password = browser.find_element(By.ID, 'reg-password-filled')
    Password.send_keys("123456")
    time.sleep(0)
    Checkbox1 = browser.find_element(By.XPATH, '//label[@data-testid="age-checkbox"]')
    Checkbox1.click()
    time.sleep(0)
    Checkbox2 = browser.find_element(By.XPATH, '//label[@data-testid="terms-checkbox"]')
    Checkbox2.click()
    time.sleep(0)
    button = browser.find_element(By.ID, 'submit-registration')
    button.click()
    time.sleep(1)
    button = browser.find_element(By.ID, 'submit-registration')
    button.click()



finally:
    time.sleep(15)
# закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла