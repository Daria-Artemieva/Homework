import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('url', ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1'])
def test_find_messages_from_aliens(browser, url):
    link = f"{url}"
    browser.get(link)

    answer = str(math.log(int(time.time())))
    print(answer)
    time.sleep(5)
    input5 = browser.find_element(By.XPATH, '//textarea[@spellcheck="false"]')
    time.sleep(3)
    input5.send_keys(answer)
    time.sleep(2)
    input6 = browser.find_element(By.XPATH, '//button[@class="submit-submission"]')
    time.sleep(2)
    input6.click()

    message = browser.find_element(By.XPATH, '//div[@class="smart-hints__hint"]').text
    print.message
    assert 'Correct!' in message

