from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://master.ci.k8s.sgr-labs.com/join/blockingcheck"


def click():
    pass


try:

    # Open the link
    browser = webdriver.Chrome()
    browser.get(link)
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(100)

    # Input the First name
    Name = browser.find_element(By.XPATH, '//input[@data-testid="mod-first-name-input"]')
    Name.send_keys("Fish")
    # Input the Last name
    Surname = browser.find_element(By.XPATH, '//input[@data-testid="mod-last-name-input"]')
    Surname.send_keys("Test5")
    # Input fake Phone number
    Phone = browser.find_element(By.ID, 'ember10')
    Phone.send_keys("+89925863403")
    # Repeat fake Phone number
    Phone2 = browser.find_element(By.XPATH, '//input[@data-testid="mod-confirm-email-input"]')
    Phone2.send_keys("+89925863403")
    # Input the Password
    Password = browser.find_element(By.XPATH, '//input[@data-testid="mod-password-input"]')
    Password.send_keys("123456")
    # Age check-box
    Checkbox1 = browser.find_element(By.ID, 'age-input')
    Checkbox1.click()
    # Agree check-box
    Checkbox2 = browser.find_element(By.ID, 'tos-input')
    Checkbox2.click()
    # Submit 1
    Submit1 = browser.find_element(By.XPATH, '//button[@data-testid="mod-sign-up-btn"]')
    Submit1.click()
    # Submit 2
    Submit2 = browser.find_element(By.XPATH, '//button[@data-testid="mod-sign-up-btn"]')
    Submit2.click()

    # Skip
    Skip = browser.find_element(By.XPATH, '//button[@class="btn btn-reset btn-back"]')
    Skip.click()
    # Skip Premium
    SkipPremium = browser.find_element(By.XPATH, '//button[@class="btn btn-reset btn-skip"]')
    SkipPremium.click()
    # Skip Interests
    SkipInterests = browser.find_element(By.CLASS_NAME, 'svg_cancel.p-absolute.top.right.mt-12.mr-12.px-6.py-6.z-1')
    SkipInterests.click()
    # Confirm Avatar
    ConfirmAvatar = browser.find_element(By.XPATH, '//button[@class="btn btn-filled btn-wider group-bg"]')
    ConfirmAvatar.click()

finally:
    time.sleep(10)
# закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла