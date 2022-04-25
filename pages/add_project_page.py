import string
import random
from selenium.webdriver.common.by import By


def get_random_string(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


project_name = get_random_string(10)
prefix = "jap" + get_random_string(6)
project_description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis"


class AddNewProjectPage:

    def __init__(self, browser):
        self.browser = browser

    def add_new_project(self):
        self.browser.find_element(By.ID, 'name').send_keys(project_name)
        self.browser.find_element(By.ID, 'prefix').send_keys(prefix)
        self.browser.find_element(By.ID, 'description').send_keys(project_description)
        self.browser.find_element(By.ID, 'save').click()

    def is_success(self):
        self.browser.find_element(By.ID, 'j_info_box')
