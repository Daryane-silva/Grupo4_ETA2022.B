import time

from pages.PIMPage import PIMPage
from pages.MenuPage import MenuPage


class TestFindEmployee:

    def test_find_employee_by_name(self, add_employee):
        menu_page = MenuPage(driver=add_employee.driver)
        menu_page.click_pim_option()

        employee_list = PIMPage(driver=menu_page.driver)
        response = employee_list.find_employee_by_name('Roberto')
        assert response, "Funcionário não encontrado"