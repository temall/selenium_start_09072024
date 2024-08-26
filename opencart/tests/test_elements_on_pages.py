from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

catalog_page = "/en-gb/catalog/laptop-notebook"
cart_page = "/en-gb?route=checkout/cart"
admin_login_page = "/administration"
registration_page = "/index.php?route=account/register"


def test_base_page(browser):
    browser.get(browser.url)
    WebDriverWait(browser, timeout=3).until(EC.visibility_of_element_located((By.ID, "carousel-banner-0")))
    WebDriverWait(browser, timeout=3).until(EC.visibility_of_element_located((By.ID, "menu")))
    WebDriverWait(browser, timeout=3).until(EC.visibility_of_element_located((By.ID, "content")))
    WebDriverWait(browser, timeout=3).until(EC.visibility_of_element_located((By.ID, "search")))
    WebDriverWait(browser, timeout=3).until(EC.visibility_of_element_located((By.CLASS_NAME, "img-fluid")))


def test_catalog_page(browser):
    browser.get(browser.url + catalog_page)
    WebDriverWait(browser, timeout=3).until(EC.visibility_of_element_located((By.ID, "column-left")))
    WebDriverWait(browser, timeout=3).until(EC.visibility_of_element_located((By.ID, "narbar-menu")))
    WebDriverWait(browser, timeout=3).until(EC.visibility_of_element_located((By.CLASS_NAME, "row")))
    WebDriverWait(browser, timeout=3).until(EC.visibility_of_element_located((By.ID, "content")))
    WebDriverWait(browser, timeout=3).until(EC.visibility_of_element_located((By.CLASS_NAME, "breadcrumb-item")))


def test_cart_page(browser):
    browser.get(browser.url + cart_page)
    WebDriverWait(browser, timeout=3).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='content']/h1")))
    WebDriverWait(browser, timeout=3).until(
        EC.visibility_of_element_located((By.XPATH, "//p[text()='Your shopping cart is empty!']")))
    WebDriverWait(browser, timeout=3).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Continue']")))


def test_admin_login_page(browser):
    browser.get(browser.url + admin_login_page)
    browser.find_element(By.ID, "input-username").clear()
    browser.find_element(By.ID, "input-username").send_keys("user")
    browser.find_element(By.ID, "input-password").clear()
    browser.find_element(By.ID, "input-password").send_keys("bitnami")
    WebDriverWait(browser, timeout=3).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='form-login']/div[3]/button"))).click()
    WebDriverWait(browser, timeout=3).until(
        EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'John Doe')]")))
    WebDriverWait(browser, timeout=3).until(EC.visibility_of_element_located((By.ID, "navigation")))
    WebDriverWait(browser, timeout=3).until(EC.visibility_of_element_located((By.ID, "stats")))
    browser.find_element(By.ID, "nav-logout").click()
    WebDriverWait(browser, timeout=3).until(EC.visibility_of_element_located((By.ID, "input-username")))


def test_registration_page(browser):
    browser.get(browser.url + registration_page)
    browser.find_element(By.ID, "input-firstname").send_keys("Toster")
    browser.find_element(By.ID, "input-lastname").send_keys("Toster")
    browser.find_element(By.ID, "input-email").send_keys("Toster@toster.toster")
    browser.find_element(By.ID, "input-password").send_keys("input-password")
    browser.find_element(By.NAME, "agree").click()
    browser.find_element(By.XPATH, "//button[text()='Continue']").click()
    WebDriverWait(browser, timeout=4).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//p[text()='Congratulations! Your new account has been successfully created!']")))


def test_currency(browser):
    browser.get(browser.url)
    price_in_dollars = browser.find_element(By.XPATH, "//span[contains(text(), '123.20')]")
    browser.find_element(By.ID, "form-currency").click()
    browser.find_element(By.XPATH, "//a[@href='EUR']").click()
    price_in_euro = browser.find_element(By.XPATH, "//span[contains(text(), '96.66')]")
    assert price_in_dollars != price_in_euro
