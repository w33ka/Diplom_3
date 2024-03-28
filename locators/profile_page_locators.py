from selenium.webdriver.common.by import By


class ProfilePageLocators:
    PROFILE_BUTTON = (By.LINK_TEXT, 'Профиль')  # кнопка "Профиль"
    ORDER_HISTORY_BUTTON = (By.LINK_TEXT, 'История заказов')  # кнопка "История заказов"
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # кнопка "Выход"
