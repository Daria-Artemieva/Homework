from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    pass

try:
    # open link
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # click on the button
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()

    # set window name
    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]

    # switch to new window
    browser.switch_to.window(new_window)
    time.sleep(2)

    # math
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    print(y)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()