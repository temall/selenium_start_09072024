import logging
import time

import allure
from playwright.sync_api import Page, expect
from opencart.pages.abstract_page import AbstractPage
from test_config import Config
from fixtures.admin_page import login

# Локаторы страницы логона
login_field = "#input-username"
password_fild = "#input-password"
login_button = "//*[text()=' Login']"
# Локаторы меню "Категории"
menu_catalog = "//*[@id='menu-catalog']/a"
menu_category = "//*[@id='collapse-1']/li[1]/a"
btn_add_new_category = "//*[@id='content']/div[1]/div/div/a"
close_red_window = "a[class='cke_notification_close']"
new_category_name = "#input-name-1"
new_category_tag = "#input-meta-title-1"
new_sort_order = "#input-sort-order"
new_key_word = "#input-keyword-0-1"
btn_save_new_category = "//*[@class='btn btn-primary']"
# Локаторы вкладок меню "Категории"
tab_general = "//*[text()='General']"
tab_data = "//*[text()='Data']"
tab_seo = "//*[text()='SEO']"
tab_design = "//*[text()='Design']"
# Локаторы меню "Продукты"
menu_products = "//*[@id='collapse-1']/li[2]/a"   
btn_add_new_product = "//*[@id='content']/div[1]/div/div/a"      
new_product_name = "#input-name-1"
new_product_tag = "#input-meta-title-1"
new_product_model = "#input-model"
new_product_price = "#input-price"
btn_save_new_product = "//*[@id='content']/div[1]/div/div/button" 
# Общие локаторы
logout_button = "//*[text()='Logout']"



class CatalogTabs:
    General = "General"
    Data = "Data"
    SEO = "SEO"
    Design = "Design"


class AdminPage(AbstractPage):
    page_path = "/administration"

    @allure.step("Открытие страницы 'Администратор'")
    def open(self):
        super().open()

    @allure.step("Вход под администратором")
    def login(self, admin_login, admin_password):
        for login in range(2):
            self.page.locator(login_field).fill(admin_login)
            self.page.locator(password_fild).fill(admin_password)
            self.page.locator(login_button).click()
            time.sleep(3)
    
    @allure.step("Получение имени залогиненного пользователя")
    def get_username(self):
        logged_user = self.page.locator("//span[contains(text(), 'John Doe')]")
        if "\xa0\xa0\xa0" in logged_user.text_content():
            logged_user = logged_user.text_content().replace("\xa0\xa0\xa0", "")
        return logged_user
    
    @allure.step("Переход на кладку {tab}")
    def open_tab(self, tab=CatalogTabs):
        if tab == CatalogTabs.General:
            self.page.locator(tab_general).click()
        elif tab == CatalogTabs.Data:
            self.page.locator(tab_data).click()
        elif tab == CatalogTabs.SEO:
            self.page.locator(tab_seo).click()
        elif tab == CatalogTabs.Design:
            self.page.locator(tab_design).click()

    @allure.step("Создание новой категории")
    def admin_add_new_category(self):
        self.page.locator(menu_catalog).click()
        time.sleep(2)
        self.page.locator(menu_category).click()
        self.page.locator(btn_add_new_category).click()
        self.page.locator(close_red_window).click()

    @allure.step("Заполнение вкладки General радела 'Категории'")
    def fill_new_category_general_tab(self, 
                                      category_name: str | None=None, 
                                      category_tag: str | None=None):
        self.page.locator(new_category_name).fill(category_name)
        self.page.locator(new_category_tag).fill(category_tag)
    
    @allure.step("Заполнение вкладки Data радела 'Категории'")
    def fill_new_category_data_tab(self,
                                   sort_order: str | None=None):
        self.page.locator(new_sort_order).fill(sort_order)

    @allure.step("Заполнение вкладки SEO радела 'Категории'")
    def fill_new_category_seo_tab(self,
                                  key_word: set | None=None):
        self.page.locator(new_key_word).fill(key_word)

    @allure.step("Сохранение новой категории")
    def save_new_category(self):
        self.page.locator(btn_save_new_category).click()

    def close_red_allert(self):
        self.page.get_by_role("button", name="Close").click()
    
    @allure.step("Создание нового продукта")
    def admin_add_new_product(self):
        self.page.locator(menu_catalog).click()
        time.sleep(3)
        self.page.locator(menu_products).click()
        self.page.locator(btn_add_new_product).click()
        self.page.locator(close_red_window).click()
    
    @allure.step("Заполнение вкладки General радела 'Продукты'")
    def fill_new_product_general_tab(self, 
                                     product_name: str | None=None, 
                                     product_tag: str | None=None):
        self.page.locator(new_product_name).fill(product_name)
        self.page.locator(new_product_tag).fill(product_tag)


    @allure.step("Заполнение вкладки Data радела 'Продукты'")
    def fill_new_product_data_tab(self,
                                  model: str | None=None):
        self.page.locator(new_product_model).fill(model)

    @allure.step("Заполнение вкладки SEO радела 'Продукты'")
    def fill_new_product_seo_tab(self,
                                 key_word: set | None=None):
        self.page.locator(new_key_word).fill(key_word)
    
    @allure.step("Сохранение нового продукта")
    def save_new_product(self):
        self.page.locator(btn_save_new_product).click()

    @allure.step("Logout администратора")
    def admin_logout(self):
        self.page.locator(logout_button).click()
    




