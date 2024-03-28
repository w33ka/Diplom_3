from selenium.webdriver.common.by import By


class RestorePasswordPageLocators:
    EMAIL_FIELD = (By.XPATH, "//input[@name='name']")  # поле Email
    RESTORE_BUTTON = (By.XPATH, '//button[text()="Восстановить"]')  # кнопка "Восстановить"
    PASSWORD_RECOVERY_HEAD = (By.XPATH, "//h2[text()='Восстановление пароля']")  # заголовок "Восстановление пароля"
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon')]")  # кнопка "Показать пароль"
    PASSWORD_FIELD_ACTIVE = (By.XPATH, "//div[contains(@class, 'input_status_active')]")  # поле Пароль активно
