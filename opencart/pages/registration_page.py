import allure

from opencart.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from opencart.pages.config import Config


class RegistrationPage(BasePage):
    input_first_name = By.ID, "input-firstname"
    input_last_name = By.ID, "input-lastname"
    input_email = By.ID, "input-email"
    input_password = By.ID, "input-password"
    privacy_policy_switcher = By.NAME, "agree"
    btn_continue = By.XPATH, "//button[text()='Continue']"

    @allure.step("Переход на страницу регисрации")
    def goto_registration_page(self):
        self.browser.get(
            "http://192.168.0.102:8081/en-gb?route=account/register")
        return self

    @allure.step("Заполнение поля 'Имя'")
    def fill_first_name(self, test_config: Config):
        self.browser.find_element(By.ID, "input-firstname").send_keys(test_config.first_name)
        self.logger.info("Поле 'Имя' заполнено")
        return self

    @allure.step("Заполнение поля 'Фамилия'")
    def fill_last_name(self, test_config: Config):
        self.browser.find_element(By.ID, "input-lastname").send_keys(test_config.last_name)
        self.logger.info("Поле 'Фамилия' заполнено")
        return self

    @allure.step("Заполнение поля 'Почта'")
    def fill_email(self, test_config: Config):
        self.browser.find_element(By.ID, "input-email").send_keys(test_config.email)
        self.logger.info("Поле 'Почта' заполнено")
        return self

    @allure.step("Заполнение поля 'Пароль'")
    def fill_password(self, test_config: Config):
        self.browser.find_element(By.ID, "input-password").send_keys(test_config.password)
        self.logger.info("Поле 'Пароль' заполнено")
        return self

    def agree_privacy_policy(self):
        self.click(self.privacy_policy_switcher)
        return self

    def press_btn_continue(self):
        self.click(self.btn_continue)
        return self
