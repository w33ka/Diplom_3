import allure

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.restore_password_page import RestorePasswordPage


class TestRestorePassword:
    @allure.title('Проверка на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_restore_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_personal_account()
        login_page = LoginPage(driver)
        login_page.click_on_restore_password_button()
        restore_password_page = RestorePasswordPage(driver)
        restore_password_page.check_password_recovery_head()

    @allure.title('Проверка ввода почты и клика по кнопке «Восстановить»')
    def test_fill_email_and_click_on_restore_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_personal_account()
        login_page = LoginPage(driver)
        login_page.click_on_restore_password_button()
        restore_password_page = RestorePasswordPage(driver)
        restore_password_page.fill_email()
        restore_password_page.click_on_restore_button()
        restore_password_page.check_show_password_button()

    @allure.title('Проверка клика по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.')
    def test_click_on_show_password_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_personal_account()
        login_page = LoginPage(driver)
        login_page.click_on_restore_password_button()
        restore_password_page = RestorePasswordPage(driver)
        restore_password_page.fill_email()
        restore_password_page.click_on_restore_button()
        restore_password_page.click_show_password_button()
        restore_password_page.check_active_field_password()






