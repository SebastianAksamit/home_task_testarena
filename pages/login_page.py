from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login(self, login, password):
        self.browser.find_element(By.ID, 'email').send_keys(login)
        self.browser.find_element(By.ID, 'password').send_keys(password)
        self.browser.find_element(By.ID, 'login').click()

    def wait_for_load_login_page(self):
        wait = WebDriverWait(self.browser, 5)
        login_button_selector = (By.ID, 'login')
        wait.until(expected_conditions.presence_of_element_located(login_button_selector))