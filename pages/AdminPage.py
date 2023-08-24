import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.PageObject import PageObject


class AdminPage(PageObject):

    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers'
    txt_admin_title = 'Admin / User Management'
    username_path = '//div[text()="Username"]'
    ascending_path = '//ul[@role="menu"]'
    ascending_class = 'oxd-table-header-sort-dropdown-item'
    table_class = 'oxd-table-body'
    table_card_class = 'oxd-table-card'
    table_cell_class = 'oxd-table-cell'


    def __init__(self, driver):
        super(AdminPage, self).__init__(driver=driver)

    def is_url_admin(self):
        return self.is_url(self.url)

    def has_admin_title(self):
        return self.has_title(self.txt_admin_title)

    def check_admin_page(self):
        return self.check_page(self.url, self.txt_admin_title)

    def open_admin_page(self):
        self.driver.get(self.url)

    def order_username(self):
        username_header = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.username_path)))
        username_header.click()
        children = username_header.find_elements(By.XPATH, './*')
        children[0].click()
        order_menu = children[0].find_element(By.XPATH, self.ascending_path)
        ascending = order_menu.find_element(By.CLASS_NAME, self.ascending_class)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(ascending))
        ascending.click()

    def check_username_order(self):
        names = []
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, self.table_class)))
        table = self.driver.find_element(By.CLASS_NAME, self.table_class)
        cards = table.find_elements(By.CLASS_NAME, self.table_card_class)
        for card in cards:
            children = card.find_elements(By.CLASS_NAME, self.table_cell_class)
            names.append(children[1].text.lower())
        for i in range(len(names)-1):
            current_name = names[i]
            next_name = names[i+1]
            if current_name > next_name:
                return False
        return True


