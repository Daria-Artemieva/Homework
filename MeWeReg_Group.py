from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://master.ci.k8s.sgr-labs.com/join/blockingcheck"


def click():
    pass


try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(5)

    Name = browser.find_element(By.XPATH, '//input[@data-testid="mod-first-name-input"]')
    Name.send_keys("Fish")
    time.sleep(0)
    Surname = browser.find_element(By.XPATH, '//input[@data-testid="mod-last-name-input"]')
    Surname.send_keys("Test3")
    time.sleep(1)
    Phone = browser.find_element(By.ID, 'ember10')
    Phone.send_keys("+89925863447")
    Phone2 = browser.find_element(By.XPATH, '//input[@data-testid="mod-confirm-email-input"]')
    Phone2.send_keys("+89925863447")
    time.sleep(0)
    Password = browser.find_element(By.XPATH, '//input[@data-testid="mod-password-input"]')
    Password.send_keys("123456")
    time.sleep(0)
    Checkbox1 = browser.find_element(By.ID, 'age-input')
    Checkbox1.click()
    time.sleep(0)
    Checkbox2 = browser.find_element(By.ID, 'tos-input')
    Checkbox2.click()
    time.sleep(0)
    Submit1 = browser.find_element(By.XPATH, '//button[@data-testid="mod-sign-up-btn"]')
    Submit1.click()
    time.sleep(2)
    Submit2 = browser.find_element(By.XPATH, '//button[@data-testid="mod-sign-up-btn"]')
    Submit2.click()
    time.sleep(5)
    Skip = browser.find_element(By.XPATH, '//button[@class="btn btn-reset btn-back"]')
    Skip.click()
    time.sleep(5)
    SkipPremium = browser.find_element(By.XPATH, '//button[@class="btn btn-reset btn-skip"]')
    SkipPremium.click()
    time.sleep(5)
    SkipInterests = browser.find_element(By.CLASS_NAME, 'svg_cancel.p-absolute.top.right.mt-12.mr-12.px-6.py-6.z-1')
    SkipInterests.click()
    time.sleep(4)
    Join = browser.find_element(By.XPATH, '//button[@class="btn btn-filled btn-wider group-bg"]')
    Join.click()
    time.sleep(3)





finally:
    time.sleep(15)
# закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла