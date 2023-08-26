from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.PageObject import PageObject


class PIMPage(PageObject):
    att_employee_name_filed = '[placeholder="Type for hints..."]'
    class_search_btn = 'orangehrm-left-space'
    class_table_body = 'oxd-table-body'
    class_table_card = 'oxd-table-card'
    class_table_row = 'oxd-table-row'
    class_cell_elements = 'oxd-table-cell'
    class_icon_checkbox = 'oxd-checkbox-input-icon'
    class_delete_btn = 'oxd-button--label-danger'
    class_edit_icon = 'bi-pencil-fill'
    xpath_firstname = '//input[@name="firstName"]'
    class_employee_name = 'orangehrm-edit-employee-name'
    class_label = 'oxd-label'
    class_save_button = 'oxd-button'
    class_grid = 'oxd-grid-3'
    class_input_nickname = 'oxd-input'
    xpath_add_employee_btn = '// *[ @ id = "app"] / div[1] / div[1] / header / div[2] / nav / ul / li[3]'

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.driver.implicitly_wait(6)

    def click_add_employee_btn(self):
        add_employee = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.xpath_add_employee_btn)))
        add_employee.click()

    def find_employee_by_name(self, employeename):
        name_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.att_employee_name_filed)))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, self.class_table_body)))
        name_field.send_keys(employeename)
        self.driver.find_element(By.CLASS_NAME, self.class_search_btn).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, self.class_table_card)))
        card_elements = self.driver.find_elements(By.CLASS_NAME, self.class_table_card)
        if len(card_elements) == 0:
            raise Exception("Funcionário não encontrado!")

        count_employee = 0
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, self.class_table_body)))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, self.class_table_row)))
        for item in card_elements:
            cell_elements = item.find_elements(By.CLASS_NAME, self.class_cell_elements)
            for cell in cell_elements:
                if employeename in cell.text:
                    count_employee += 1

        if count_employee > 0:
            return True
        else:
            return False

    def delete_employee_by_name(self, employeename):
        found_employee = self.find_employee_by_name(employeename)
        if not found_employee:
            return False
        else:
            self.driver.find_element(By.CLASS_NAME, self.class_icon_checkbox).click()
            delete_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, self.class_delete_btn)))
            delete_btn.click()
            super().click_yes_delete_btn_modal()
            self.driver.find_element(By.CLASS_NAME, self.class_search_btn).click()
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, self.class_table_body)))
            card_elements = self.driver.find_elements(By.CLASS_NAME, self.class_table_card)
            if len(card_elements) == 0:
                return True
            else:
                return False

    def verify_edit_success(self, nickname):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, self.class_grid)))
        grid_items = self.driver.find_elements(By.CLASS_NAME, self.class_grid)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, self.class_input_nickname)))
        for item in grid_items:
            if item.find_element(By.CLASS_NAME, self.class_label).text == 'Nickname':
                nick2 = item.find_element(By.CLASS_NAME, self.class_input_nickname).get_attribute("value")
                if nickname == nick2:
                    return True
                else:
                    return False
        return False

    def edit_employee(self, firstname, middlename, lastname, nickname):
        employeename = firstname + " " + middlename
        found_employee = self.find_employee_by_name(employeename)
        if not found_employee:
            return False
        else:
            self.driver.find_element(By.CLASS_NAME, self.class_edit_icon).click()
            WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element_value((By.XPATH, self.xpath_firstname), firstname))
            if self.driver.find_element(By.CLASS_NAME, self.class_employee_name).text == firstname + ' ' + lastname:
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, self.class_grid)))
                grid_items = self.driver.find_elements(By.CLASS_NAME, self.class_grid)
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, self.class_input_nickname)))
                for item in grid_items:
                    if item.find_element(By.CLASS_NAME, self.class_label).text == "Nickname":
                        nickname_edt = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, self.class_input_nickname)))
                        nickname_edt.send_keys(Keys.BACKSPACE * len(item.find_element(By.CLASS_NAME, self.class_input_nickname).get_attribute("value")))
                        item.find_element(By.CLASS_NAME, self.class_input_nickname).send_keys(nickname)
                        save_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, self.class_save_button)))
                        save_btn.click()
                return self.verify_edit_success(nickname)
            else:
                return False
