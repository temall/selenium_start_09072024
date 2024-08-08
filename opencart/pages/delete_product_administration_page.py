import time

from selenium.webdriver.common.by import By
from opencart.pages.base_page import BasePage


class AdminDeleteProductPage(BasePage):
    menu_catalog = By.CSS_SELECTOR, "#menu-catalog"
    menu_products = By.CSS_SELECTOR, "#collapse-1 li:nth-child(2)"
    last_page = By.XPATH, "//*[@id='form-product']/div[2]/div[1]/ul/li[2]/a"
    last_product = By.XPATH, "//form[@id='form-product']//tbody//tr[last()]"
    product_checkbox = By.XPATH, "//form[@id='form-product']//tbody//tr[last()]//input"
    btn_delete_product = By.XPATH, "//button[@title='Delete']"

    def open_products(self):
        self.click(self.menu_catalog)
        self.click(self.menu_products)
        return self

    def go_to_last_page(self):
        self.browser.execute_script("window.scrollTo(0, window.scrollY + 200)")
        self.click(self.last_page)
        return self

    def select_product(self):
        self.browser.execute_script("window.scrollTo(0, window.scrollY + 200)")
        self.click(self.last_product)
        return self

    def select_checkbox(self):
        self.click(self.product_checkbox)
        return self

    def delete_product(self):
        self.click(self.btn_delete_product)
        time.sleep(3)
        return self

    def accept_delete_product(self):
        self.get_alert()
