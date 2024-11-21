import logging
import time

import allure
from playwright.sync_api import Page, expect
from opencart.pages.abstract_page import AbstractPage

# Локаторы
search_field = "#search"
search_button = "//*[@id='search']/button"
tab_desktop = "//*[text()='Desktops']"
tab_laptops_notebook = "//*[text()='Laptops & Notebooks']"
tab_components = "//*[text()='Components']"
tab_tablets = "//*[text()='Tablets']"
tab_software = "//*[text()='Software']"
tab_phones = "//*[text()='Phones & PDAs']"
tab_cameras = "//*[text()='Cameras']"
tab_mp3_players = "//*[text()='MP3 Players']"
# Локаторы карточки товара
price = "//*[@id='product-list']//*[@class='price-new']"
add_to_cart = "//*[@method='post']//*[@class='fa-solid fa-shopping-cart']"
add_to_wishlist = "//*[@method='post']//*[@class='fa-solid fa-heart']"
compare_product = "//*[@method='post']//*[@class='fa-solid fa-arrow-right-arrow-left']"
# Локаторы тележки
open_cart = "//*[@id='top']//*[@title='Shopping Cart']"
total_price = "//*[@id='checkout-total']/tr[4]/td[2]"
# Лоаторы выбора валюты
_currency = "//*[text()='Currency']"
euro = "//*[@id='form-currency']//*[text()='€ Euro']"
pound = "//*[@id='form-currency']//*[text()='£ Pound Sterling']"
us = "//*[@id='form-currency']//*[text()='$ US Dollar']"


class BasePageTabs:
    Desktop = "Desktop"
    Laptop_Notebooks = "Laptop_Notebooks"
    Components = "Components"
    Tablets = "Tablets"
    Software = "Software"
    Phones_PDAs = "Phones_PDAs"
    Cameras = "Cameras"
    MP3_Players = "MP3_Players"


class Currency:
    Euro = "Euro"
    Pound = "Pound"
    US = "US"


class BasePage(AbstractPage):
    page_path = ""

    @allure.step("Открытие основной страницы")
    def open(self):
        super().open()

    @allure.step("Переход на кладку {tab}")
    def open_tab(self, tab=BasePageTabs):
        if tab == BasePageTabs.Desktop:
            self.page.locator(tab_desktop).click()
        elif tab == BasePageTabs.Laptop_Notebooks:
            self.page.locator(tab_laptops_notebook).click()
        elif tab == BasePageTabs.Components:
            self.page.locator(tab_components).click()
        elif tab == BasePageTabs.Tablets:
            self.page.locator(tab_tablets).click()
        elif tab == BasePageTabs.Software:
            self.page.locator(tab_software).click()
        elif tab == BasePageTabs.Phones_PDAs:
            self.page.locator(tab_phones).click()
        elif tab == BasePageTabs.Cameras:
            self.page.locator(tab_cameras).click()
        elif tab == BasePageTabs.MP3_Players:
            self.page.locator(tab_mp3_players).click()

    @allure.step("Выбор валюты {currency}")
    def change_currency(self, currency=Currency):
        self.page.locator(_currency).click()
        time.sleep(0.5)
        if currency == Currency.Euro:
            self.page.locator(euro).click()
        elif currency == Currency.Pound:
            self.page.locator(pound).click()
        elif currency == Currency.US:
            self.page.locator(us).click()

    @allure.step("Поиск товара в строке 'Поиск'")
    def search_item(self,
                    item: str | None = None):
        self.page.locator(search_field).get_by_placeholder("Search").fill(item)
        self.page.locator(search_button).click()
        time.sleep(1)

    @allure.step("Добавление товара в корзину")
    def add_to_cart(self):
        self.page.locator(add_to_cart).click()

    @allure.step("Добавление товара в wishlist")
    def add_to_wishlist(self):
        self.page.locator(add_to_wishlist).click()

    @allure.step("Добавление товара для сравнения")
    def add_to_compare(self):
        self.page.locator(compare_product).click()

    def get_added_notification(self):
        success_added = self.page.locator("//*[@class='alert alert-success alert-dismissible']")
        return success_added.text_content()

    @allure.step("Переход в корзину товаров")
    def open_cart(self):
        self.page.locator(open_cart).click()

    @allure.step("Проверка стоимости набранного товара")
    def check_total_price(self):
        return self.page.locator(total_price).text_content()
