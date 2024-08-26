import allure
import logging
from selenium.webdriver.common.by import By
from opencart.pages.add_product_administration_page import AdminAddProductPage
from opencart.pages.delete_product_administration_page import AdminDeleteProductPage
from opencart.pages.registration_page import RegistrationPage
from opencart.pages.main_page import MainPage


@allure.step("Добавление нового продукта на странице администрирования")
def test_admin_add_new_product(browser, admin_login):
    new_product = AdminAddProductPage(browser)
    new_product.open_products()
    new_product.click_add_new_product()
    new_product.set_product_name()
    new_product.set_product_meta_tag()
    new_product.go_to_data_tab()
    new_product.set_product_model_name()
    new_product.set_product_price()
    new_product.set_product_quantity()
    new_product.go_to_seo_tab()
    new_product.set_product_seo()
    new_product.save_new_product()
    assert new_product.successful_alert()


@allure.step("Удаление последнего продукта на странице администрирования")
def test_admin_delete_product(browser, admin_login):
    delete_product = AdminDeleteProductPage(browser)
    delete_product.open_products()
    delete_product.go_to_last_page()
    delete_product.select_product()
    delete_product.select_checkbox()
    delete_product.delete_product()
    delete_product.accept_delete_product()
    assert delete_product.successful_alert()


@allure.step("Регистрация нового пользователя")
def test_registration_page(browser, test_config):
    registration = RegistrationPage(browser)
    registration.goto_registration_page()
    registration.fill_first_name(test_config)
    registration.fill_last_name(test_config)
    registration.fill_email(test_config)
    registration.fill_password(test_config)
    registration.agree_privacy_policy()
    registration.press_btn_continue()
    assert registration.successful_registration_alert()


@allure.step("Изменение валюты из верхнего меню")
def test_change_currency(browser):
    price = MainPage(browser)
    price.open_main_page()
    iphone_price_in_dollars = browser.find_element(By.XPATH, "//span[contains(text(), '123.20')]")
    price.choose_currency()
    price.set_euro_currency()
    iphone_price_in_euros = browser.find_element(By.XPATH, "//span[contains(text(), '96.66')]")
    assert iphone_price_in_dollars != iphone_price_in_euros
    price.choose_currency()
    price.set_pound_sterling_currency()
    iphone_price_in_pound = browser.find_element(By.XPATH, "//span[contains(text(), '75.46')]")
    assert iphone_price_in_euros != iphone_price_in_pound
