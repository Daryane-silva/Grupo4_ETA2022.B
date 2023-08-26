from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class DashboardPage(PageObject):

    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
    txt_dashboard_title = 'Dashboard'
    xpath_shortcut = '//button[@class="orangehrm-quick-launch-icon"]'

    def __init__(self, driver):
        super(DashboardPage, self).__init__(driver=driver)
        self.driver.implicitly_wait(3)

    def is_url_dashboard(self):
        return self.is_url(self.url)

    def has_dashboard_title(self):
        return self.has_title(self.txt_dashboard_title)

    def check_dashboard_page(self):
        return self.check_page(self.url, self.txt_dashboard_title)

    def click_shortcut(self, shortcut_name):
        shortcut_buttons = self.driver.find_elements(By.XPATH, self.xpath_shortcut)
        for button in shortcut_buttons:
            if button.text == shortcut_name:
                button.click()
