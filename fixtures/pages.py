import pytest
from playwright.sync_api import Page

from opencart.pages.admin_page import AdminPage
from opencart.pages.base_page import BasePage
from opencart.pages.registration_page import RegistrationPage


@pytest.fixture
def admin_page(page: Page):
    return AdminPage(page)

@pytest.fixture
def base_page(page: Page):
    return BasePage(page)

@pytest.fixture
def reg_page(page: Page):
    return RegistrationPage(page)
