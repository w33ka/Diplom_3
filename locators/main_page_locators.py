from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.LINK_TEXT, 'Конструктор')  # кнопка "Конструктор"

    ORDERS_FEED_BUTTON = (By.LINK_TEXT, 'Лента Заказов')  # кнопка "Лента заказов"

    PERSONAL_ACCOUNT_BUTTON = (By.LINK_TEXT, 'Личный Кабинет')  # кнопка "Личный кабинет"

    CONSTRUCTOR_HEAD = (By.XPATH, '//h1[text()="Соберите бургер"]')  # заголовок в конструкторе "Соберите бургер"

    ORDERS_FEED_HEAD = (By.XPATH, "//h1[contains(text(), 'Лента заказов')]")  # заголовок в ленте заказов

    INGREDIENT = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")  # ингридиент

    INGREDIENT_DETAILS_HEAD = (By.XPATH, '//h2[text()="Детали ингредиента"]')  # окно с деталями об ингредиенте

    CLOSE_BUTTON = (By.XPATH, "(//button[@type='button'])[1]")  # кнопка крестик в окне с деталями об ингредиенте

    BASKET = (By.CLASS_NAME, "BurgerConstructor_basket__list__l9dp_")  # корзина конструктора

    INGREDIENT_COUNTER = (By.XPATH, "//ul[1]/a[1]//p[contains(@class, 'num')]")  # счетчик ингредиента

    ORDER_BUTTON = (By.XPATH, "//button[text() = 'Оформить заказ']")  # кнопка "Оформить заказ"

    ORDER_WINDOW = (By.XPATH, "//div[@class='Modal_modal__container__Wo2l_']")  # окно после оформления заказа

    ORDER_CARD = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')]")  # карточка заказа в Ленте заказов

    ORDER_DETAILS = (By.XPATH, "//div[contains(@class, 'Modal_orderBox')]")  # окно с деталями о заказе

    ORDER_NUMBER = (By.XPATH, '//p[contains(@class, "text text_type_digits")]')  # номер заказа в ленте и в истории

    ALL_TIME_COUNTER = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number')])[1]")  # cчетчик заказов за все время

    DAY_COUNTER = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number')])[2]")  # счетчик закзов за день

    ORDER_ID = (By.XPATH, '//h2[contains(@class, "Modal_modal__title_shadow")]')  # номер заказа в окне после создания

    SECTION_IN_WORK = (By.XPATH, f"//li[contains(text(), '0')]")  # раздел "В работе"



