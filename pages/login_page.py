import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step('Нажатие на кнопку "Восстановить пароль"')
    def click_on_restore_password_button(self):
        self.click_on_element(LoginPageLocators.RESTORE_PASSWORD_BUTTON)

    @allure.step('Проверка что открылась форма авторизации')
    def check_login_head(self):
        self.find_element(LoginPageLocators.LOGIN_HEAD)

    @allure.step('Авторизация на сайте')
    def login(self, email, password):
        self.set_text_on_element(LoginPageLocators.EMAIL_FIELD, email)
        self.set_text_on_element(LoginPageLocators.PASSWORD_FIELD, password)
        self.click_on_element(LoginPageLocators.LOGIN_BUTTON)

