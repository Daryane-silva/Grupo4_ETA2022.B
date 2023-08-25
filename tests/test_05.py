from pages.PIMPage import PIMPage
from pages.MenuPage import MenuPage


class Test05:

    def test_delete_employee_by_name(self, add_employee):
        menu_page = MenuPage(driver=add_employee.driver)
        menu_page.click_pim_option()

        employee_list = PIMPage(driver=menu_page.driver)
        response = employee_list.delete_employee_by_name("Roberto Mendes")
        assert response, "Erro na exclusão de funcionário"
