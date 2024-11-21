import allure
import pytest

from playwright.sync_api import Page
from test_config import Config


pytest_plugins = [
    "fixtures.pages",
]


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Позволяет получать информацию о результате теста в фикстурах используемых тестами"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    if call.when == "call" and call.excinfo is not None and "page" in item.funcargs:
        page: Page = item.funcargs["page"]
        allure.attach(page.screenshot(type='png'),
                      name=f"{item.nodeid}.png",
                      attachment_type=allure.attachment_type.PNG)

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    """Добавляет аргументы для браузера"""
    return {
        **browser_type_launch_args,
        "args": ["--start-maximized", "--incognito"],
    }

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Убирает viewport, иначе нельзя открыть браузер на весь экран"""
    return {
        **browser_context_args,
        "no_viewport": True
    }

@pytest.fixture()
def test_config():
    config = Config()
    yield config
