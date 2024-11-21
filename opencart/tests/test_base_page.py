import allure
import pytest

from playwright.sync_api import Page
from opencart.pages.base_page import BasePage, Currency


item_for_search = "test_for_search"
nonexisting_item = "bla-bla-lba"
found_item = f"//*[@id='product-list']//*[text()='{item_for_search}']"
not_found_item = f"//*[@id='content']//*[text()='There is no product that matches the search criteria.']"
item_price = "//*[@id='product-list']//*[@class='price-new']"

pytestmark = allure.suite("Основная страница")


@allure.title("Првоерка поиска товара")
@pytest.mark.search
def test_search_itemsearch_item(page: Page,
                     base_page: BasePage):
    base_page.open()
    base_page.search_item(f"{item_for_search}")
    result = page.locator(found_item)
    assert result.text_content() == item_for_search

@allure.title("Првоерка поиска несуществующего товара")
@pytest.mark.search
def test_bad_search(page: Page,
                   base_page: BasePage):
    base_page.open()
    base_page.search_item(f"{nonexisting_item}")
    result = page.locator(not_found_item)
    assert result.text_content() == "There is no product that matches the search criteria."

@allure.title("Првоерка смены валюты")
@pytest.mark.change_currency
def test_change_crrency(page: Page,
                        base_page: BasePage):
    base_page.open()
    base_page.search_item("Iphone")
    iphone_price_in_dollar = page.locator(item_price).text_content()
    assert iphone_price_in_dollar == "$123.20"
    base_page.change_currency(Currency.Euro)
    page.reload()
    base_page.search_item("Iphone")
    iphone_price_in_euro = page.locator(item_price).text_content()
    assert iphone_price_in_euro == "96.66€"
    base_page.change_currency(Currency.Pound)
    page.reload()
    base_page.search_item("Iphone")
    iphone_price_in_pound = page.locator(item_price).text_content()
    assert iphone_price_in_pound == "£75.46"

@allure.title("Првоерка соответствия стоимости товара в карточке товара и в корзине")
@pytest.mark.add_to_cart
def test_add_to_cart(page: Page,
                     base_page: BasePage):
    base_page.open()
    base_page.search_item("Iphone")
    iphone_price_ = page.locator(item_price).text_content()
    base_page.add_to_cart()
    assert base_page.get_added_notification() == " Success: You have added iPhone to your shopping cart! "
    base_page.open_cart()
    assert base_page.check_total_price() == iphone_price_
