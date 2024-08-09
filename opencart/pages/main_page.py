from opencart.pages.base_page import BasePage
from selenium.webdriver.common.by import By

import allure


class MainPage(BasePage):
    price_in_dollars = By.XPATH, "//span[contains(text(), '123.20')]"
    all_currency = By.ID, "form-currency"
    euro = By.XPATH, "//a[@href='EUR']"
    dollar = By.XPATH, "//a[@href='USD']"
    pound = By.XPATH, "//a[@href='GBP']"

    @allure.step("Открытие главное страницы")
    def open_main_page(self):
        self.browser.get("http://192.168.0.102:8081")

    @allure.step("Открытие списка валют")
    def choose_currency(self):
        self.click(self.all_currency)
        return self

    @allure.step("Выбор валюты в долларах")
    def set_dollar_currency(self):
        self.click(self.dollar)
        return self

    @allure.step("Выбор валюты в евро")
    def set_euro_currency(self):
        self.click(self.euro)
        return self

    @allure.step("Выбор валюты в фунтах")
    def set_pound_sterling_currency(self):
        self.click(self.pound)


