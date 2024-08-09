from opencart.pages.base_page import BasePage
from selenium.webdriver.common.by import By

import allure


class AdminPage(BasePage):
    login_button = By.CSS_SELECTOR, "button[type=submit]"

    @allure.step("Переход на страницу администрирования")
    def goto_admin_page(self):
        self.browser.get("http://192.168.0.102:8081/administration/index.php?route=common/login")
        self.logger.info("Осуществлен переход на траницу администрирования")

    @allure.step("Ввод логина администратора")
    def input_login(self):
        self.browser.find_element(By.ID, "input-username").send_keys("user")
        return self

    @allure.step("Ввод пароля администратора")
    def input_password(self):
        self.browser.find_element(By.ID, "input-password").send_keys("bitnami")
        return self

    @allure.step("Нажатие кнопки 'Login'")
    def login(self):
        self.click(self.login_button)
        self.logger.info("Успешный вход")
        return self
