from pages.AssignLeavePage import AssignLeavePage
from pages.DashboardPage import DashboardPage


class Test08:

    def test_menu_list(self, login_orangerh):
        dashboard_page = DashboardPage(driver=login_orangerh.driver)
        dashboard_page.click_shortcut('Assign Leave')
        assign_leave_page = AssignLeavePage(dashboard_page.driver)
        assert assign_leave_page.check_assign_leave_page(), 'Página não encontrada'
