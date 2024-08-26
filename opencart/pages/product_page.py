from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class ProductPage:

    def __init__(self, browser: WebDriver):
        self.browser = browser

    def click_add_to_cart(self):
        self.browser.find_element(By.CSS_SELECTOR, "#button-cart").click()

    def click_add_to_comparison(self):
        self.browser.find_element(By.CSS_SELECTOR, "[title='Compare this Product']").click()

    def clil_add_to_wish_list(self):
        self.browser.find_element(By.CSS_SELECTOR, "[title='Add to Wish List']").click()

