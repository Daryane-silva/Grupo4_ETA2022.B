
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.PageObject import PageObject


class LoginPage(PageObject):
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    login_button = '[type="submit"]'
    username = '[name="username"]'
    password = '[name="password"]'

    def __init__(self, browser):
        super(LoginPage, self).__init__(browser=browser)
        self.driver.get(self.url)

    def click_login_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.login_button).click()

    def is_url_login(self):
        return self.driver.current_url == self.url

    def efetuar_login(self, username='Admin', password='admin123'):
        usernamefield = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.username)))
        usernamefield.send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, self.password).send_keys(password)
        self.click_login_btn()

