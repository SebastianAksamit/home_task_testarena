from selenium.webdriver.common.by import By

class ProjectViewPage:
    def __init__(self, browser):
        self.browser = browser

    def go_to_projects(self):
        # self.browser.find_element(By.CSS_SELECTOR, '#wrapper > ul > li.item2 > a').click()
        self.browser.find_element(By.CLASS_NAME, "item2").click()