from selenium.webdriver.common.by import By
from opencart.pages.base_page import BasePage


class AdminPage(BasePage):

    login_button = By.CSS_SELECTOR, "button[type=submit]"

    def goto_admin_page(self):
        self.browser.get("http://192.168.0.102:8081/administration/index.php?route=common/login")

    def input_login(self):
        self.browser.find_element(By.ID, "input-username").send_keys("user")
        return self

    def input_password(self):
        self.browser.find_element(By.ID, "input-password").send_keys("bitnami")
        return self

    def login(self):
        self.click(self.login_button)
        return self

