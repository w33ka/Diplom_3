import pytest
from selenium import webdriver

import helpers
import requests
from data import Urls, UrlsApi
from pages.main_page import MainPage
from pages.login_page import LoginPage


@pytest.fixture(params=["chrome"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.get(Urls.BASE_URL)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.get(Urls.BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def user_registration(driver):
    payload = helpers.payload
    response = requests.post(UrlsApi.REGISTER_USER, json=payload)
    token = response.json().get('accessToken')
    yield payload, token

    headers = {'Authorization': f'Bearer {token}'}
    requests.delete(UrlsApi.DELETE_USER, headers=headers)


@pytest.fixture
def login(driver, user_registration):
    payload, token = user_registration
    email = payload["email"]
    password = payload["password"]
    main_page = MainPage(driver)
    main_page.click_on_personal_account()
    login_page = LoginPage(driver)
    login_page.login(email, password)
    return driver
