import allure
import pytest

from playwright.sync_api import Page
from test_config import Config
from opencart.pages.admin_page import AdminPage, CatalogTabs
from fixtures.admin_page import login


success_added_category = " Success: You have modified categories! "
success_added_product = " Success: You have modified products! "
product_already_exist = " Warning: Please check the form carefully for errors! "
success_notification = "//*[@class='alert alert-success alert-dismissible']"
warning_notification = "//*[@class='alert alert-danger alert-dismissible']"
login_button = "//*[text()=' Login']"

pytestmark = allure.suite("Страница администратора")


@allure.title("Првоерка входа под администратором")
@pytest.mark.admin_login
def test_admin_login(page: Page,
                     test_config: Config,
                     admin_page: AdminPage):
    page.goto(test_config.url)
    admin_page.open()
    admin_page.login(test_config.admin_login, test_config.admin_password)
    assert admin_page.get_username() == "John Doe "

@allure.title("Првоерка выхода из под администратора")
@pytest.mark.admin_logout
def test_admin_logut(login, page: Page, admin_page: AdminPage):
    admin_page.admin_logout()
    assert page.locator(login_button).is_visible()

@allure.title("Првоерка добавления новой категории администратором")
@pytest.mark.add_category
def test_add_new_category(login, page: Page, admin_page: AdminPage):
    admin_page.admin_add_new_category()
    admin_page.fill_new_category_general_tab(category_name="3333", category_tag="3333")
    admin_page.open_tab(CatalogTabs.Data)
    admin_page.fill_new_category_data_tab(sort_order="3333")
    admin_page.open_tab(CatalogTabs.SEO)
    admin_page.fill_new_category_seo_tab(key_word="3333")
    admin_page.open_tab(CatalogTabs.Design)
    admin_page.save_new_category()
    notification =  page.locator(success_notification)
    catrgory_created = notification.text_content()
    assert catrgory_created == success_added_category

@allure.title("Првоерка добавления нового продукта администратором")
@pytest.mark.add_product
def test_add_new_product(login, page: Page, admin_page: AdminPage):
    admin_page.admin_add_new_product()
    admin_page.fill_new_product_general_tab(product_name="new_product3", product_tag="new_product3")
    admin_page.open_tab(CatalogTabs.Data)
    admin_page.fill_new_product_data_tab(model="new_product3")
    admin_page.open_tab(CatalogTabs.SEO)
    admin_page.fill_new_product_seo_tab(key_word="new_product3")
    admin_page.save_new_product()
    notification =  page.locator(success_notification)
    product_created = notification.text_content()
    assert product_created == success_added_product

@allure.title("Првоерка добавления уже существующего продукта администратором")
@pytest.mark.add_same_product
def test_add_same_product(login, page: Page, admin_page: AdminPage):
    admin_page.admin_add_new_product()
    admin_page.fill_new_product_general_tab(product_name="1s1", product_tag="s11")
    admin_page.open_tab(CatalogTabs.Data)
    admin_page.fill_new_product_data_tab(model="1s1")
    admin_page.open_tab(CatalogTabs.SEO)
    admin_page.fill_new_product_seo_tab(key_word="11s")
    admin_page.save_new_product()
    notification =  page.locator(warning_notification)
    product_created = notification.text_content()
    assert product_created == product_already_exist
