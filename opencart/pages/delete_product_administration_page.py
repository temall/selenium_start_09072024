from opencart.pages.base_page import BasePage
from selenium.webdriver.common.by import By

import allure
import time


class AdminDeleteProductPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    menu_catalog = By.CSS_SELECTOR, "#menu-catalog"
    menu_products = By.CSS_SELECTOR, "#collapse-1 li:nth-child(2)"
    last_page = By.XPATH, "//*[@id='form-product']/div[2]/div[1]/ul/li[2]/a"
    last_product = By.XPATH, "//form[@id='form-product']//tbody//tr[last()]"
    product_checkbox = By.XPATH, "//form[@id='form-product']//tbody//tr[last()]//input"
    btn_delete_product = By.XPATH, "//button[@title='Delete']"

    @allure.step("Открытие раздела 'Продукты'")
    def open_products(self):
        self.click(self.menu_catalog)
        self.click(self.menu_products)
        return self

    @allure.step("Переход на последнюю страницу")
    def go_to_last_page(self):
        self.browser.execute_script("window.scrollTo(0, window.scrollY + 200)")
        self.click(self.last_page)
        return self

    @allure.step("Выбор последнего продукта")
    def select_product(self):
        self.browser.execute_script("window.scrollTo(0, window.scrollY + 200)")
        self.click(self.last_product)
        return self

    @allure.step("Выбор чекбокса продукта")
    def select_checkbox(self):
        self.click(self.product_checkbox)
        return self

    @allure.step("Нажатие на кнопку удаления продукта")
    def delete_product(self):
        self.click(self.btn_delete_product)
        self.logger.info("Удаление продукта")
        time.sleep(3)
        return self

    @allure.step("Подтверждение удаления продукта")
    def accept_delete_product(self):
        self.get_alert()
        self.logger.info("Продукт успешно удален")
