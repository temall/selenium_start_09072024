import time

import pytest
from playwright.sync_api import Page
from test_config import Config


login_field = "#input-username"
password_fild = "#input-password"
login_button = "//*[text()=' Login']"


@pytest.fixture
def login(page: Page, test_config: Config):
    page.goto("localhost:8081/administration/")
    for login in range(2):
        page.locator(login_field).fill(test_config.admin_login)
        page.locator(password_fild).fill(test_config.admin_password)
        page.locator(login_button).click()
        time.sleep(2)
