from pages.PIMPage import PIMPage
from pages.AddEmployeePage import AddEmployeePage
from pages.MenuPage import MenuPage


class Test02:

    firstname = 'Roberto'
    middlename = 'Mendes'
    lastname = 'Menezes'

    def test_add_new_employee(self, login_orangerh):
        menu_page = MenuPage(driver=login_orangerh.driver)
        menu_page.click_pim_option()
        pim_page = PIMPage(driver=menu_page.driver)
        pim_page.click_add_employee_btn()
        new_employee = AddEmployeePage(driver=menu_page.driver)
        new_employee.add_new_employee(self.firstname, self.middlename, self.lastname)
        response = new_employee.verify_details_new_employee(self.firstname, self.lastname)
        assert response, "Funcionário não encontrado"
