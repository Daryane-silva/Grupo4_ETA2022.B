from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.PageObject import PageObject


class BuzzPage(PageObject):
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz'
    class_post = 'oxd-buzz-post-input'
    xpath_post_button = '//button[@type="submit"]'
    xpath_post_body = '//p[@class="oxd-text oxd-text--p orangehrm-buzz-post-body-text"]'

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.driver.implicitly_wait(3)
        self.driver.get(self.url)

    def write_post(self, post_text):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, self.class_post)))
        post_edit = self.driver.find_element(By.CLASS_NAME, self.class_post)
        post_edit.send_keys(post_text)

    def click_post(self):
        post_button = self.driver.find_element(By.XPATH, self.xpath_post_button)
        post_button.click()

    def buzz_post(self, post_text):
        self.write_post(post_text)
        self.click_post()

    def check_post(self, post_text):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.xpath_post_body)))
            post_list = self.driver.find_elements(By.XPATH, self.xpath_post_body)
            for post in post_list:
                if post.text == post_text:
                    return True
            return False
        except:
            return False
