from pages.PIMPage import PIMPage
from pages.MenuPage import MenuPage


class Test04:

    def test_edit_employee_by_name(self, add_employee):
        menu_page = MenuPage(driver=add_employee.driver)
        menu_page.click_pim_option()

        employee_list = PIMPage(driver=menu_page.driver)
        result = employee_list.edit_employee('Roberto', 'Mendes', 'Menezes', 'Beto')
        assert result, "Erro na edição do funcionário"