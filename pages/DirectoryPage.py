from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.PageObject import PageObject


class DirectoryPage(PageObject):
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/directory/viewDirectory'
    att_employee_name_filed = '[placeholder="Type for hints..."]'
    class_search_btn = 'orangehrm-left-space'
    class_card = 'orangehrm-directory-card'
    class_cell_elements = 'oxd-table-cell'
    class_dropdown = 'oxd-autocomplete-dropdown'
    class_directory_card = 'orangehrm-directory-card'


    def __init__(self, driver):
        super().__init__(driver=driver)
        self.driver.implicitly_wait(3)
        self.driver.get(self.url)

    def find_employee_by_name(self, employeename):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.att_employee_name_filed)))
        self.driver.find_element(By.CSS_SELECTOR, self.att_employee_name_filed).send_keys(employeename)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, self.class_dropdown)))
        dropdown = self.driver.find_element(By.CLASS_NAME, self.class_dropdown)
        try:
            WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, self.class_dropdown), employeename))
        except:
            raise Exception("Funcionário não encontrado!")
        dropdown.click()
        self.driver.find_element(By.CLASS_NAME, self.class_search_btn).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, self.class_card)))
        card_elements = self.driver.find_elements(By.CLASS_NAME, self.class_card)
        if len(card_elements) == 0:
            raise Exception("Funcionário não encontrado!")

        count_employee = 0
        for item in card_elements:
            child = item.find_element(By.TAG_NAME, 'p')
            if employeename in child.text:
                count_employee += 1

        if count_employee > 0:
            return True
        else:
            return False

    def show_employee_detail(self, employeename):
        card_elements = self.driver.find_elements(By.CLASS_NAME, self.class_card)
        for item in card_elements:
            child = item.find_element(By.TAG_NAME, 'p')
            if employeename in child.text:
                child.click()

    def check_employee_detail(self, employeename):
        directory_card = self.driver.find_element(By.CLASS_NAME, self.class_directory_card)
        return employeename in directory_card.text
