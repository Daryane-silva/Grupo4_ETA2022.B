from selenium.webdriver.common.by import By

from pages.PageObject import PageObject
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AssignLeavePage(PageObject):
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/leave/assignLeave'
    txt_title = 'Leave'
    class_title_page = 'oxd-topbar-header-breadcrumb'

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.driver.implicitly_wait(3)
        self.driver.get(self.url)

    def is_url_dashboard(self):
        return self.is_url(self.url)

    def has_dashboard_title(self):
        return self.has_title(self.txt_title)

    def check_assign_leave_page(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, self.class_title_page)))
        return self.check_page(self.url, self.txt_title)
