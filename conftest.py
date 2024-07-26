import pytest
from selenium import webdriver


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
