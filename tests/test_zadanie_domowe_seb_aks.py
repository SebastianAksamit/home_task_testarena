import config
import pytest
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from pages.add_project_page import AddNewProjectPage
from pages.admin_page import AdminPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.project_view_page import ProjectViewPage
from pages.projects_page import ProjectsPage


@pytest.fixture()
def browser():
    browser = Chrome(executable_path=ChromeDriverManager().install())
    browser.get('http://demo.testarena.pl/zaloguj')
    yield browser
    browser.quit()


def test_create_new_project_in_admin_panel(browser):
    login_page = LoginPage(browser)
    login_page.wait_for_load_login_page()
    login_page.login(config.login, config.password)

    home_page = HomePage(browser)
    home_page.wait_for_load_home_page()
    home_page.go_to_admin_panel()

    admin_page = AdminPage(browser)
    admin_page.wait_for_load_admin_page()
    admin_page.add_new_project()

    add_project_page = AddNewProjectPage(browser)
    add_project_page.add_new_project()
    add_project_page.is_success()

    project_view_page = ProjectViewPage(browser)
    project_view_page.go_to_projects()

    projects_page = ProjectsPage(browser)
    projects_page.search_new_added_project()
