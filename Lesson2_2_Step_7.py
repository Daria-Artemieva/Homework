from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # заполняем обязательные поля
    FirstName = browser.find_element(By.XPATH, '//input[@placeholder="Enter first name"]')
    FirstName.send_keys("Dasha")
    LastName = browser.find_element(By.XPATH, '//input[@placeholder="Enter last name"]')
    LastName.send_keys("Art")
    Email = browser.find_element(By.XPATH, '//input[@placeholder="Enter email"]')
    Email.send_keys("dar@gmail.com")

    # получаем путь к директории текущего исполняемого скрипта lesson2_7.py
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # имя файла, который будем загружать на сайт
    file_name = "file.txt"
    # получаем путь к file.txt
    file_path = os.path.join(current_dir, file_name)
    # отправляем файл
    element = browser.find_element(By.ID, 'file')
    element.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()