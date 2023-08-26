from pages.AdminPage import AdminPage


class Test01:

    def test_order_username(self, login_orangerh):
        admin_p = AdminPage(driver=login_orangerh.driver)
        admin_p.open_admin_page()
        assert admin_p.is_url_admin(), 'Página Admin não encontrada!'
        admin_p.order_username()
        assert admin_p.check_username_order(), 'Nomes dos usuários não foram ordenados!'
