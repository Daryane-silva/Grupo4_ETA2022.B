import time

import pytest

from pages.LoginPage import LoginPage


def pytest_addoption(parser):
    parser.addoption("--select_browser", default="chrome", help="Select browser")


@pytest.fixture
def select_browser(request):
    yield request.config.getoption("--select_browser").lower()


@pytest.fixture()
def setup(select_browser):
    login_page = LoginPage(browser=select_browser)
    yield login_page
    login_page.close()


@pytest.fixture
def login_orangerh(setup):
    login_page = setup
    login_page.efetuar_login()
    yield login_page



