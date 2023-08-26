from pages.DirectoryPage import DirectoryPage
from pages.MenuPage import MenuPage


class Test06:

    def test_employee_detail(self, add_employee):
        menu_page = MenuPage(driver=add_employee.driver)
        menu_page.click_directory_option()
        directory_page = DirectoryPage(driver=menu_page.driver)
        assert directory_page.find_employee_by_name('Roberto'), 'Funcionário não encontrado'
        directory_page.show_employee_detail('Roberto')
        assert directory_page.check_employee_detail('Roberto'), 'Detalhes não correspondem ao usuário encontrado'
