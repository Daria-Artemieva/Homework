from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    pass


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    print(y)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

    Checkbox1 = browser.find_element(By.ID, 'robotCheckbox')
    Checkbox1.click()

    Option2 = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", Option2)
    Option2.click()
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()