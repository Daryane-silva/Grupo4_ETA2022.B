import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.PageObject import PageObject


class PIMPage(PageObject):

    att_employee_name_filed = '[placeholder="Type for hints..."]'
    class_search_btn = 'orangehrm-left-space'
    class_table_card = 'oxd-table-card'
    class_cell_elements = 'oxd-table-cell'
    class_header_col = 'oxd-table-header-cell'
    class_btn_sort = 'oxd-table-header-sort'
    class_component_sort = 'oxd-table-header-sort-dropdown-item'
    class_icon_checkbox = 'oxd-checkbox-input-icon'
    class_delete_btn = 'oxd-button--label-danger'
    class_edit_icon = 'bi-pencil-fill'
    class_employee_name = 'orangehrm-edit-employee-name'
    class_label = 'oxd-label'
    class_input = 'oxd-input--active'
    class_save_button = 'oxd-button'
    class_grid = 'oxd-grid-3'
    class_input_nickname = 'oxd-input'
    xpath_add_employee_btn = '// *[ @ id = "app"] / div[1] / div[1] / header / div[2] / nav / ul / li[3]'

    def __init__(self, driver):
        super().__init__(driver=driver)

    def click_add_employee_btn(self):
        add_employee = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((
            By.XPATH, self.xpath_add_employee_btn)))
        add_employee.click()

    def find_employee_by_name(self, employeename):
        self.driver.find_element(By.CSS_SELECTOR, self.att_employee_name_filed).send_keys(employeename)
        time.sleep(3)
        self.driver.find_element(By.CLASS_NAME, self.class_search_btn).click()
        time.sleep(3)
        card_elements = self.driver.find_elements(By.CLASS_NAME, self.class_table_card)
        if len(card_elements) == 0:
            raise Exception("Funcionário não encontrado!")

        count_employee = 0
        for item in card_elements:
            cell_elements = item.find_elements(By.CLASS_NAME, self.class_cell_elements)
            for cell in cell_elements:
                if employeename in cell.text:
                    count_employee += 1

        if count_employee >0:
            return True
        else:
            return False

    def select_column_header(self, col_name):
        header_col = self.driver.find_elements(By.CLASS_NAME, self.class_header_col)
        selected_col = ''
        for item in header_col:
            if item.text == col_name:
                selected_col = item
                break
        return selected_col

    def click_component_order_in_selected_column(self, select_col_name):
        col_element = self.select_column_header(select_col_name)
        time.sleep(2)
        btn_sort = col_element.find_element(By.CLASS_NAME, self.class_btn_sort)
        btn_sort.click()

    def select_order(self, order_type):
        ord_elements = self.driver.find_elements(By.CLASS_NAME, self.class_component_sort)
        selected_order = ''
        for item in ord_elements:
            if item.text == order_type:
                selected_order = item
                break
        return selected_order

    def order_employee_list_order_asc(self, col_name='First (& Middle) Name', order_type='Ascending'):
        self.click_component_order_in_selected_column(col_name)
        time.sleep(2)
        self.select_order(order_type).click()
        time.sleep(2)

    def check_order_first_name_asc(self):
        all_employees = self.driver.find_elements(By.CLASS_NAME, self.class_table_card)
        employee_list = []

        for i in range(len(all_employees)):
            css_first_name_element = '#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div.orangehrm-paper-container > div.orangehrm-container > div > div.oxd-table-body > div:nth-child('+ str(i+1) +') > div > div:nth-child(3) > div'
            first_name_element = self.driver.find_element(By.CSS_SELECTOR, css_first_name_element)
            employee_list.append(first_name_element.text)

        employee_list_copy = employee_list.copy()
        employee_list_upper = [x.upper() for x in employee_list]
        employee_list_copy_upper = [x.upper() for x in employee_list_copy]
        employee_list_copy_upper.sort()
        print(f'\nLista ordenada pela aplicação: {employee_list_upper}')
        print(f'Lista ordenada pelo código como resultado esperado: {employee_list_copy_upper}')


        if employee_list_upper == employee_list_copy_upper:
            return True
        return False

    def delete_employee_by_name(self, employeename):
        found_employee = self.find_employee_by_name(employeename)
        if not found_employee:
            return False
        else:
            self.driver.find_element(By.CLASS_NAME, self.class_icon_checkbox).click()
            time.sleep(3)
            self.driver.find_element(By.CLASS_NAME, self.class_delete_btn).click()
            time.sleep(3)

            super().click_yes_delete_btn_modal()

            # clicando novamente em Search para validar que o funcionário não foi encontrado
            self.driver.find_element(By.CLASS_NAME, self.class_search_btn).click()
            time.sleep(3)
            card_elements = self.driver.find_elements(By.CLASS_NAME, self.class_table_card)
            if len(card_elements) == 0:
                return True
            else:
                return False

    def edit_employee(self, firstname, middlename, lastname, nickname):
        employeename = firstname + " " + middlename
        found_employee = self.find_employee_by_name(employeename)
        if not found_employee:
            return False
        else:
            self.driver.find_element(By.CLASS_NAME, self.class_edit_icon).click()
            time.sleep(3)
            # validando que na tela de editar é o nome do funcionário correto
            if self.driver.find_element(By.CLASS_NAME, self.class_employee_name).text == firstname + ' ' + lastname:
                time.sleep(3)
                grid_items = self.driver.find_elements(By.CLASS_NAME, self.class_grid)
                time.sleep(5)
                for item in grid_items:
                    if item.find_element(By.CLASS_NAME, self.class_label).text == "Nickname":
                        time.sleep(2)
                        item.find_element(By.CLASS_NAME, self.class_input_nickname).send_keys(
                            Keys.BACKSPACE * len(item.find_element(By.CLASS_NAME, self.class_input_nickname).get_attribute("value")))
                        item.find_element(By.CLASS_NAME, self.class_input_nickname).send_keys(nickname)
                        time.sleep(3)
                        self.driver.find_element(By.CLASS_NAME, self.class_save_button).click()
                        time.sleep(3)
                return self.verify_edit_success(nickname)
            else:
                return False

    def verify_edit_success(self, nickname):
        grid_items = self.driver.find_elements(By.CLASS_NAME, self.class_grid)
        time.sleep(5)
        for item in grid_items:
            if item.find_element(By.CLASS_NAME, self.class_label).text == 'Nickname':
                nick2 = item.find_element(By.CLASS_NAME, self.class_input_nickname).get_attribute("value")
                if nickname == nick2:
                    return True
                else:
                    return False
        return False
