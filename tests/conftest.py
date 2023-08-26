import pytest

from pages.AddEmployeePage import AddEmployeePage
from pages.LoginPage import LoginPage
from pages.MenuPage import MenuPage
from pages.PIMPage import PIMPage


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

@pytest.fixture()
def add_employee(login_orangerh):
    menu_page = MenuPage(driver=login_orangerh.driver)
    menu_page.click_pim_option()
    pim_page = PIMPage(driver=menu_page.driver)
    pim_page.click_add_employee_btn()
    new_employee = AddEmployeePage(driver=menu_page.driver)
    new_employee.add_new_employee('Roberto', 'Mendes', 'Menezes')
    yield new_employee



