from selenium.webdriver.common.by import By
from opencart.pages.base_page import BasePage


class AdminAddProductPage(BasePage):
    menu_catalog = By.CSS_SELECTOR, "#menu-catalog"
    menu_products = By.CSS_SELECTOR, "#collapse-1 li:nth-child(2)"
    add_new_product = By.CSS_SELECTOR, "i[class='fa-solid fa-plus']"
    close_red_window = By.CSS_SELECTOR, "a[class='cke_notification_close']"

    def open_products(self):
        self.click(self.menu_catalog)
        self.click(self.menu_products)
        return self

    def click_add_new_product(self):
        self.click(self.add_new_product)
        self.click(self.close_red_window)
        return self

    def set_product_name(self):
        self.browser.find_element(By.ID, "input-name-1").send_keys("TestProduct")
        return self

    def set_product_meta_tag(self):
        self.browser.find_element(By.ID, "input-meta-title-1").send_keys("TestTag")

    def go_to_data_tab(self):
        self.browser.find_element(By.XPATH, "//*[@id='form-product']/ul/li[2]/a").click()
        return self

    def set_product_model_name(self):
        self.browser.find_element(By.ID, "input-model").send_keys("TestModel")
        return self

    def set_product_price(self):
        self.browser.find_element(By.ID, "input-price").send_keys("100500")
        return self

    def set_product_quantity(self):
        self.browser.find_element(By.ID, "input-quantity").send_keys("123")
        return self

    def go_to_seo_tab(self):
        self.browser.find_element(By.XPATH, "//*[@id='form-product']/ul/li[11]/a").click()
        return self

    def set_product_seo(self):
        self.browser.find_element(By.ID, "input-keyword-0-1").send_keys("SEO")
        return self

    def save_new_product(self):
        self.browser.find_element(By.CSS_SELECTOR, "#content > div.page-header > div > div > button").click()
        return self
