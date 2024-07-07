from pages.recovery_password_page import RecoveryPasswordPage
from pages.main_page import MainPage
import allure


class TestMainPage:

    @allure.title('Проверка перехода по клику на кнопку "Конструктор"')
    @allure.description('Проверяем переход в Конструктор заказа бургера по клику на кнопку "Конструктор" со страницы авторизации')
    def test_switch_to_constructor_by_button_successful(self, driver):
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.click_button_login()
        main_page = MainPage(driver)
        main_page.click_button_constructor()

        assert 'Соберите бургер' in main_page.get_title_of_constructor_order()

    @allure.title('Проверка открытия окна "Детали ингредиента" при клике на ингредиент')
    @allure.description('Проверяем, что при клике на ингридиенте в Конструкторе - открывается окно "Детали ингредиента"')
    def test_opening_window_details_of_ingredient_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient_burger()

        assert main_page.check_openinng_window_details_of_ingredient()
        assert main_page.get_title_of_window_details_of_ingredient() == 'Детали ингредиента'

    @allure.title('Проверка закрытия окна "Детали ингредиента" при клике по кнопке с крестиком этого окна')
    @allure.description('Проверяем закрытие окна "Детали ингредиента", ранее открытого по клику на ингредиент')
    def test_closing_window_details_of_ingredient_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient_burger()
        main_page.click_to_close_window_details_of_ingredient()

        assert main_page.check_closing_window_details_of_ingredient()

    @allure.title('Проверка увеличения числа на счетчике при добавлении ингредиента в заказ')
    @allure.description('Проверяем увеличение числа ингредиентов в заказе при переносе ингредиентов в "корзину"')
    def test_changing_counter_for_ingredients_in_order_success(self, driver):
        main_page = MainPage(driver)
        main_page.drag_and_drop_ingredient_into_basket()

        assert main_page.get_count_of_ingredients_into_basket() == '2'

    @allure.title('Залогиненный пользователь может оформить заказ')
    @allure.description('Проверяем, что пользователь залогиненный при помощи фикстуры может создать заказ на сайте')
    def test_making_order_by_authenticated_user_success(self, driver, login_user):
        main_page = MainPage(driver)
        main_page.button_make_order_is_appeared()
        main_page.drag_and_drop_ingredient_into_basket()
        main_page.click_button_make_order()

        assert main_page.check_window_confirmation_order_is_displayed()
        assert main_page.get_order_status_in_window_confirmation() == 'Ваш заказ начали готовить'
