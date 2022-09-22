import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('url', ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1',
                                 'https://stepik.org/lesson/236897/step/1', 'https://stepik.org/lesson/236898/step/1',
                                 'https://stepik.org/lesson/236899/step/1', 'https://stepik.org/lesson/236903/step/1',
                                 'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1'])
def test_find_messages_from_aliens(browser, url):
    link = f"{url}"
    browser.get(link)

    answer = str(math.log(int(time.time())))
    print(answer)

    browser.find_element(By.XPATH, '//textarea[@spellcheck="false"]').send_keys(answer)

    browser.find_element(By.XPATH, '//button[@class="submit-submission"]').click()

    message = browser.find_element(By.XPATH, '//p[@class="smart-hints__hint"]').text
    print(message)
    assert 'Correct!' in message, 'Не сходится'

