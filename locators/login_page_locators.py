from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_HEAD = (By.XPATH, "//h2[text()='Вход']")  # заголовок "Вход"
    EMAIL_FIELD = (By.XPATH, "//input[@name='name']")  # поле Email
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']")  # поле Пароль
    LOGIN_BUTTON = (By.XPATH, '//button[(text()="Войти")]')  # кнопка "Войти"
    RESTORE_PASSWORD_BUTTON = (By.LINK_TEXT, "Восстановить пароль")  # кнопка "Восстановить пароль"


