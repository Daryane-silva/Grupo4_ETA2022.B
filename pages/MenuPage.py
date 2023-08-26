from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.PageObject import PageObject


class MenuPage(PageObject):

    id_menu_btn = 'react-burger-menu-btn'
    att_pim_option = '[href="/web/index.php/pim/viewPimModule"]'
    att_directory_option = '[href="/web/index.php/directory/viewDirectory"]'
    att_buzz_option = '[href="/web/index.php/buzz/viewBuzz"]'
    xpath_menu = '//ul[@class="oxd-main-menu"]'
    class_menu_item = 'oxd-main-menu-item'

    def __init__(self, driver):
        super(MenuPage, self).__init__(driver=driver)
        self.driver.implicitly_wait(10)

    def open_menu(self):
        self.driver.find_element(By.ID, self.id_menu_btn).click()

    def click_pim_option(self):
        pim_option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, self.att_pim_option)))
        pim_option.click()

    def click_directory_option(self):
        directory_option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.att_directory_option)))
        directory_option.click()

    def click_buzz_option(self):
        buzz_option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.att_buzz_option)))
        buzz_option.click()

    def check_menu_list(self, menu_list):
        menu = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.xpath_menu)))
        menu_items = menu.find_elements(By.CLASS_NAME, self.class_menu_item)
        list_menu_item_name = list()
        for menu_item in menu_items:
            list_menu_item_name.append(menu_item.text)
        return list_menu_item_name == menu_list
