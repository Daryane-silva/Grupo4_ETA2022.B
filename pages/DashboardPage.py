

from pages.PageObject import PageObject


class DashboardPage(PageObject):

    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
    txt_dashboard_title = 'Dashboard'


    def __init__(self, driver):
        super(DashboardPage, self).__init__(driver=driver)

    def is_url_dashboard(self):
        return self.is_url(self.url)

    def has_dashboard_title(self):
        return self.has_title(self.txt_dashboard_title)

    def check_dashboard_page(self):
        return self.check_page(self.url, self.txt_dashboard_title)
