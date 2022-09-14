from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    pass


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    Treasure = browser.find_element(By.ID, 'treasure')
    x = Treasure.get_attribute("valuex")

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    Checkbox1 = browser.find_element(By.ID, 'robotCheckbox')
    Checkbox1.click()
    Option1 = browser.find_element(By.ID, 'peopleRule')
    Option1.click()
    Option2 = browser.find_element(By.ID, 'robotsRule')
    Option2.click()
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()