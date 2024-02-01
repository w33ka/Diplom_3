import allure

from locators.restore_password_page_locators import RestorePasswordPageLocators
from pages.base_page import BasePage
from helpers import fake


class RestorePasswordPage(BasePage):
    @allure.step('Проверка что открылась страница "Восстановление пароля"')
    def check_password_recovery_head(self):
        return self.find_element(RestorePasswordPageLocators.PASSWORD_RECOVERY_HEAD).text

    @allure.step('Заполнение поля "Email"')
    def fill_email(self):
        email = fake.email()
        self.set_text_on_element(RestorePasswordPageLocators.EMAIL_FIELD, email)

    @allure.step('Нажатие на кнопку "Восстановить"')
    def click_on_restore_button(self):
        self.click_on_element(RestorePasswordPageLocators.RESTORE_BUTTON)

    @allure.step('Проверка что кнопка "Показать/скрыть пароль" отображается')
    def check_show_password_button(self):
        self.find_element(RestorePasswordPageLocators.SHOW_PASSWORD_BUTTON)

    @allure.step('Нажатие на кнопку "Показать/скрыть пароль"')
    def click_show_password_button(self):
        self.click_on_element(RestorePasswordPageLocators.SHOW_PASSWORD_BUTTON)

    @allure.step('Проверка что поле "Пароль" активно')
    def check_active_field_password(self):
        self.find_element(RestorePasswordPageLocators.PASSWORD_FIELD_ACTIVE)







