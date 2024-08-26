from opencart.pages.base_page import BasePage
from selenium.webdriver.common.by import By

import allure


class AdminAddProductPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    menu_catalog = By.CSS_SELECTOR, "#menu-catalog"
    menu_products = By.CSS_SELECTOR, "#collapse-1 li:nth-child(2)"
    add_new_product = By.CSS_SELECTOR, "i[class='fa-solid fa-plus']"
    close_red_window = By.CSS_SELECTOR, "a[class='cke_notification_close']"

    @allure.step("Открытие раздела 'Продукты'")
    def open_products(self):
        self.click(self.menu_catalog)
        self.click(self.menu_products)
        return self

    @allure.step("Нажатие на кнопку 'Добавить новый продукт'")
    def click_add_new_product(self):
        self.click(self.add_new_product)
        self.click(self.close_red_window)
        self.logger.info("Начато создание нового продукта")
        return self

    @allure.step("Заполение поля 'Наименования продукта'")
    def set_product_name(self):
        self.browser.find_element(By.ID, "input-name-1").send_keys("TestProduct")
        return self

    @allure.step("Заполение поля тэга продукта")
    def set_product_meta_tag(self):
        self.browser.find_element(By.ID, "input-meta-title-1").send_keys("TestTag")

    @allure.step("Переход на вкладку 'Data'")
    def go_to_data_tab(self):
        self.browser.find_element(By.XPATH, "//*[@id='form-product']/ul/li[2]/a").click()
        return self

    @allure.step("Заполнение поля 'Модель продукта'")
    def set_product_model_name(self):
        self.browser.find_element(By.ID, "input-model").send_keys("TestModel")
        return self

    @allure.step("Заполнение поля 'Стоимость продукта'")
    def set_product_price(self):
        self.browser.find_element(By.ID, "input-price").send_keys("100500")
        return self

    @allure.step("Заполнение поля 'Количество продукта'")
    def set_product_quantity(self):
        self.browser.find_element(By.ID, "input-quantity").send_keys("123")
        return self

    @allure.step("Заполнение поля 'Стоимость продукта'")
    def go_to_seo_tab(self):
        self.browser.find_element(By.XPATH, "//*[@id='form-product']/ul/li[11]/a").click()
        return self

    @allure.step("Заполнение поля 'Ключевое слово'")
    def set_product_seo(self):
        self.browser.find_element(By.ID, "input-keyword-0-1").send_keys("SEO")
        return self

    @allure.step("Нажатие на кнопку 'Сохранить новйы продукт'")
    def save_new_product(self):
        self.browser.find_element(By.CSS_SELECTOR, "#content > div.page-header > div > div > button").click()
        self.logger.info("Новый продукт успешно создан")
        return self
