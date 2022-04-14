from selenium.webdriver.common.by import By

class ProjectsPage:
    def __init__(self, browser):
        self.browser = browser

    def search_new_added_project(self):
        from pages.add_project_page import project_name
        self.browser.find_element(By.ID, 'search').send_keys(project_name)
        self.browser.find_element(By.ID,'j_searchButton').click()
        assert self.browser.find_element(By.CSS_SELECTOR, 'td > a').text == project_name


