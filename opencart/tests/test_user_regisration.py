import allure
import pytest

from playwright.sync_api import Page
from opencart.pages.registration_page import RegistrationPage

congratulations = "Congratulations! Your new account has been successfully created!"
mail_error = "E-Mail Address does not appear to be valid!"

pytestmark = allure.suite("Страница регистрации")


@allure.title("Првоерка регистрации нового пользователя")
@pytest.mark.valid_registration
def test_user_registration_valid(page: Page,
                           reg_page: RegistrationPage):
    reg_page.open()
    reg_page.user_regisration(user_first_name="111111111", user_last_name="111111111", user_email="test6@mail.ru", user_password="1111111")
    assert reg_page.get_success_registration_message() == congratulations

@allure.title("Првоерка регистрации пользователя с некорректной почтой")
@pytest.mark.invalid_registration
def test_user_registration_valid(page: Page,
                           reg_page: RegistrationPage):
    reg_page.open()
    reg_page.user_regisration(user_first_name="11111111", user_last_name="11111111", user_email="1@1.1", user_password="111111")
    assert reg_page.get_mail_error() == mail_error
