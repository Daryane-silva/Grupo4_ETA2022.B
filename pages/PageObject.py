from selenium import webdriver
from selenium.webdriver.common.by import By


class PageObject:
    #class_title_page = '[""]'
    class_option_popup_delete = 'orangehrm-modal-footer'

    def __init__(self, driver=None, browser=None):
        if driver:
            self.driver = driver
        else:
            if browser == 'chrome':
                self.driver = webdriver.Chrome()
            elif browser == 'safari':
                self.driver = webdriver.Safari()
            elif browser == 'firefox':
                self.driver = webdriver.Firefox()
            elif browser == 'edge':
                self.driver = webdriver.Edge()
            else:
                raise Exception('Browser não suportado!')
            self.driver.maximize_window()

    def close(self):
        self.driver.quit()

    def is_url(self, url):
        return self.driver.current_url == url

    def has_title(self, title_text):
        title_page = self.driver.find_element(By.CSS_SELECTOR, self.class_title_page).text
        return title_page == title_text

    def check_page(self, url, title_text):
        return self.is_url(url) and self.has_title(title_text)

    def click_yes_delete_btn_modal(self):
        option = 'Yes, Delete'
        options_popup_delete = self.driver.find_elements(By.CLASS_NAME, self.class_option_popup_delete)
        for i in range(len(options_popup_delete)):
            current_option = options_popup_delete[i]
            if option in current_option.text:
                current_option.click()
