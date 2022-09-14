from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button1 = browser.find_element(By.ID, "submit_button")
    button1.click()

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
