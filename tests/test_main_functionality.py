import allure

from pages.main_page import MainPage


class TestMainFunctionality:
    @allure.title(' Переход по клику на «Конструктор»')
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_personal_account()
        main_page.click_on_constructor()
        main_page.check_constructor_section()

    @allure.title(' Переход по клику на «Лента заказов»')
    def test_go_to_orders_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_orders_feed()
        main_page.check_orders_feed_section()

    @allure.title('Проверка всплывающего окна с деталями при нажатии на ингредиент')
    def test_open_window_ingredient_details(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        main_page.check_ingredient_details_window()

    @allure.title('Проверка закрытия всплывающего окна с деталями об ингредиенте')
    def test_close_window_ingredient_details(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        main_page.close_details_window()
        main_page.check_close_ingredient_details_window()

    @allure.title('Проверка увеличения счетчика ингредиента, при добавлении его в заказ')
    def test_add_ingredient_to_order(self, driver):
        main_page = MainPage(driver)
        before_add = main_page.get_ingredient_counter()
        main_page.add_ingredients_to_order()
        after_add = main_page.get_ingredient_counter()
        assert after_add > before_add

    @allure.title('Проверка что залогиненный пользователь может оформить заказ')
    def test_make_order_by_authorized_user(self, driver, login):
        main_page = MainPage(driver)
        main_page.add_ingredients_to_order()
        main_page.click_order_button()
        main_page.check_order_window()




