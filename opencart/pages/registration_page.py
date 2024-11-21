import logging
import time

import allure
from playwright.sync_api import Page, expect
from opencart.pages.abstract_page import AbstractPage

# Локаторы
first_name = "#input-firstname"
last_name = "#input-lastname"
email = "#input-email"
password = "#input-password"
privacy_agree = "//*[@class='text-end']//*[@class='form-check-input']"
btn_continue = "//*[@class='btn btn-primary']"


class RegistrationPage(AbstractPage):
    page_path = "/index.php?route=account/register"


    @allure.step("Открытие страницы регистрации")
    def open(self):
        super().open()

    @allure.step("Регистрация пользователя")
    def user_regisration(self,
                         user_first_name: str | None=None,
                         user_last_name: str | None=None,
                         user_email: str | None=None,
                         user_password: str | None=None):
        # Почему то регистрация проходит только со второго раза
        for reg in range(2):
            self.page.locator(first_name).fill(user_first_name)
            self.page.locator(last_name).fill(user_last_name)
            self.page.locator(email).fill(user_email)
            self.page.locator(password).fill(user_password)
            self.page.locator(privacy_agree).click()
            self.page.locator(btn_continue).click()
            time.sleep(2)

    def get_success_registration_message(self):
        return self.page.locator("//*[text()='Congratulations! Your new account has been successfully created!']").text_content()
    
    def get_mail_error(self):
        return self.page.locator("//*[@id='error-email']").text_content()
        

    