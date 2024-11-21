import logging
import allure
from playwright.sync_api import Page, expect, Locator

from test_config import Config


class OptionNotFoundException(Exception):
    ...


class AbstractPage:
    page_path: str

    def __init__(self, page: Page):
        self.page = page
        self.test_config = Config()
        self.logger = logging.getHandlerByName(self.test_config.logger_name)

    @allure.step("Переход на страницу по ссылке")
    def open(self):
        self.page.goto(self.test_config.url + self.page_path)
