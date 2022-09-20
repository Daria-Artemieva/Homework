from selenium import webdriver

# Указываем полный путь к geckodriver.exe на вашем ПК.
driver = webdriver.Firefox('C:\geckodriver')
driver.get("http://www.google.com")