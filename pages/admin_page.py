from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class AdminPage:
    def __init__(self, browser):
        self.browser = browser

    def wait_for_load_admin_page(self):
        wait = WebDriverWait(self.browser, 5)
        search_bar = (By.ID, 'search')
        wait.until(expected_conditions.presence_of_element_located(search_bar))

    def add_new_project(self):
        self.browser.find_element(By.CLASS_NAME, 'button_link_li').click()
