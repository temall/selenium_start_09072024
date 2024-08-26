import pytest
from selenium import webdriver
from opencart.pages.admin_page import AdminPage
from opencart.pages.config import Config


def pytest_addoption(parser):
    parser.addoption("--browser", default="ch")
    parser.addoption("--url", default="http://192.168.0.102:8081/")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    url = request.config.getoption("--url")

    if browser_name == "ch":
        driver = webdriver.Chrome()
    elif browser_name == "ff":
        driver = webdriver.Firefox()

    driver.set_window_size(1920, 1080)
    driver.url = url

    yield driver

    driver.quit()


@pytest.fixture()
def admin_login(browser):
    admin_page = AdminPage(browser)
    admin_page.goto_admin_page()
    admin_page.input_login()
    admin_page.input_password()
    admin_page.login()

    return admin_page


@pytest.fixture()
def test_config():
    config = Config()
    yield config
