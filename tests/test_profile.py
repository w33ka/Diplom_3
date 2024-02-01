import allure

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


class TestProfile:
    @allure.title('Переход по клику на «Личный кабинет»')
    def test_go_to_personal_account(self, driver, login):
        main_page = MainPage(driver)
        main_page.click_on_personal_account()
        profile_page = ProfilePage(driver)
        profile_page.check_profile_button()

    @allure.title('Переход в раздел «История заказов»')
    def test_go_to_order_history(self, driver, login):
        main_page = MainPage(driver)
        main_page.click_on_personal_account()
        profile_page = ProfilePage(driver)
        profile_page.click_on_order_history_button()
        profile_page.check_order_history_section()

    @allure.title('Проверка выхода из аккаунта')
    def test_logout(self, driver, login):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.click_on_personal_account()
        profile_page = ProfilePage(driver)
        profile_page.click_on_logout_button()
        login_page.check_login_head()





