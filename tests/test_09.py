from pages.BuzzPage import BuzzPage
from pages.MenuPage import MenuPage


class Test09:

    def test_buzz_post(self, login_orangerh):
        post_text = 'Parabéns Maria Eduarda'
        menu_page = MenuPage(driver=login_orangerh.driver)
        menu_page.click_buzz_option()
        buzz_page = BuzzPage(driver=menu_page.driver)
        buzz_page.buzz_post(post_text=post_text)
        assert buzz_page.check_post(post_text=post_text), 'Post não encontrado'
