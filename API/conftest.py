import allure
import pytest
import requests


class Client:
    def __init__(self, base_url):
        self.base_address = base_url

    def get(self, path="/", params=None, headers=None):
        url = f"{self.base_address}{path}"
        with allure.step(f"GET request to: {url}"):
            return requests.get(url=url, params=params, headers=headers)

    def post(self, path="/", params=None, data=None, json=None, headers=None):
        url = f"{self.base_address}{path}"
        with allure.step(f"POST request to: {url}"):
            return requests.post(url=url, params=params, data=data, json=json, headers=headers)


@pytest.fixture
def dog_api():
    return Client(base_url="https://dog.ceo/api/")
