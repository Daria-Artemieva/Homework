from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://master.ci.k8s.sgr-labs.com/"


def click():
    pass


try:
    browser = webdriver.Chrome()
    browser.get(link)

    Name = browser.find_element(By.ID, 'reg-first-filled')
    Name.send_keys("Daria")
    time.sleep(0)
    Surname = browser.find_element(By.ID, 'reg-last-filled')
    Surname.send_keys("Test")
    time.sleep(0)
    Email = browser.find_element(By.ID, 'reg-email-filled')
    Email.send_keys("dartest17@groupl.es")
    time.sleep(0)
    EmailRepeat = browser.find_element(By.ID, 'reg-email-filled-repeat')
    EmailRepeat.send_keys("dartest17@groupl.es")
    time.sleep(0)
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



finally:
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла