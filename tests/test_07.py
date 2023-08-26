from pages.MenuPage import MenuPage


class Test07:

    def test_menu_list(self, login_orangerh):
        menu_list = ['Admin', 'PIM', 'Leave', 'Time', 'Recruitment', 'My Info', 'Performance', 'Dashboard', 'Directory', 'Maintenance', 'Claim', 'Buzz']

        menu_page = MenuPage(driver=login_orangerh.driver)
        assert menu_page.check_menu_list(menu_list), 'Menu divergente do esperado'
