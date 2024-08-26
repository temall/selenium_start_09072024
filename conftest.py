from opencart.pages.admin_page import AdminPage
from opencart.pages.config import Config
from selenium.webdriver import ChromeOptions, FirefoxOptions
from selenium import webdriver

import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", default="ch")
    parser.addoption("--url", default="http://192.168.0.102:8081/")
    parser.addoption("--remote", action="store_true")
    parser.addoption("--executor", action="store", default="192.168.0.102")
    parser.addoption("--bv", action="store", defult="127.0")
    parser.addoption("--vnc", action="store_true")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    remote = request.config.getoption("--remote")
    executor = request.config.getoption("--executor")
    browser_version = request.config.getoption("--bv")
    vnc = request.config.getoption("--vnc")

    if remote:
        executor_url = f"https://{executor}:4444/wd/hub"
        if browser_name == "ch":
            options = ChromeOptions()
        elif browser_name == "ff":
            options = FirefoxOptions()

        caps = {"browserName": browser_name,
                "browserVersion": browser_version,
                "selenoid:options": {"enableVNC": vnc,
                                     "name": request.node.name,
                                     "screenResolution": "1920x1080",
                                     "enableLog"
                                     "timeZone": "Europe/Moscow",
                                     "env": ["LANG=ru_RU.UTF-8", "LANGUAGE=ru:en", "LC_ALL=ru_RU.UTF-8"]},
                "acceptInsecureCerts": True}
        for k, v in caps.items():
            options.set_capability(k, v)

        driver = webdriver.Remote(command_executor=executor_url,
                                  options=options)

    else:
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
