from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    success_alert = By.CSS_SELECTOR, ".alert-success"
    successful_registration = By.XPATH, "//p[text()='Congratulations! Your new account has been successfully created!']"

    def __init__(self, browser):
        self.browser = browser

    def open_page(self):
        self.browser.get("http://192.168.0.102:8081")

    def get_element(self, locator: tuple, timeout=5):
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    def click(self, locator: tuple):
        ActionChains(self.browser).move_to_element(self.get_element(locator)).pause(1).click().perform()

    def get_alert(self):
        WebDriverWait(self.browser, 5).until(EC.alert_is_present()).accept()

    def successful_alert(self):
        self.get_element(self.success_alert)
        return self

    def successful_registration_alert(self):
        self.get_element(self.successful_registration)
        return self
