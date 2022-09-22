import time
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


class TestItemPage:

    def test_button_add_to_basket_is_visible(self, browser):
        # Open item page
        browser.get(link)

        # time sleep
        time.sleep(5)

        # Check ig item page contains 'Add to basket' button
        assert browser.find_element(By.XPATH, '//button[@type="submit"]')