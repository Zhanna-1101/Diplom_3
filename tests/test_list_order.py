from pages.personal_account_page import PersonalAccountPage
from pages.list_orders_page import ListOrdersPage
from pages.main_page import MainPage
from locators.locators_list_order_page import LocatorsListOrderPage as loc_list_order
from data_static import Urls as url
import pytest
import allure


class TestListOrdersPage:

    @allure.title('Проверка перехода по клику на "Лента заказов"')
    @allure.description('Проверяем переход на Ленту заказов с главной страницы сайта, кликом по кнопке "Лента заказов"')
    def test_switch_to_list_orders_by_button_successful(self, driver):
        list_order_page = ListOrdersPage(driver)
        list_order_page.click_button_list_orders()

        assert list_order_page.get_current_page_url() == url.LIST_PAGE_URL
        assert list_order_page.get_title_list_order() == 'Лента заказов'

    @allure.title('Проверка открытия окна содержащего детали заказа при клике на карточку заказа')
    @allure.description('Проверяем открытие окна, содержащего детали заказа путем клика по нему на странице с лентой заказов')
    def test_opening_window_with_order_details_successful(self, driver):
        list_order_page = ListOrdersPage(driver)
        list_order_page.click_button_list_orders()
        list_order_page.wait_card_order_to_be_clicable()
        list_order_page.click_card_order()

        assert list_order_page.check_open_card_order_in_list_order()

    @allure.title('Проверка отображения в Ленте заказов заказа из истории пользователя в ленте')
    @allure.description('Проверяем, что заказ, созданный авторизованным при помощи фикстуры пользователем, \
                        отражается в Истории заказов пользователя и в Ленте заказов')
    def test_information_about_user_order_displays_in_list_orders_and_history_orders_successful(self, driver, login_user):
        main_page = MainPage(driver)
        main_page.make_order()
        account_page = PersonalAccountPage(driver)
        account_page.click_button_personal_account()
        account_page.waiting_url_profile()
        account_page.click_button_order_history()
        order_id = account_page.get_order_number()
        list_order_page = ListOrdersPage(driver)
        list_order_page.click_button_list_orders()
        list_order_page.get_title_list_order()
        order_list_text = list_order_page.get_numbers_all_orders()
        assert order_id in order_list_text

    @pytest.mark.parametrize('counter', [loc_list_order.COMPLETED_ORDERS_ALL_TIME, loc_list_order.COMPLETED_ORDERS_TODAY])
    @allure.title('Проверка увеличения числа на счетчике общего количества выполненных заказов/в счетчике заказов за день')
    @allure.description('Проверяем увеличение чисел на счетчиках: (1)общего количества заказов, (2)заказов за день \
                        при создании заказа авторизованным, при помощи фикстуры пользователем')
    def test_changes_counter_for_all_time_quantity_of_orders_success(self, driver, counter, login_user):
        list_order_page = ListOrdersPage(driver)
        list_order_page.click_button_list_orders()
        list_order_page.waiting_url_list_order()
        list_order_page.wait_card_order_to_be_clicable()
        counter_before_order = list_order_page.get_quantity_of_orders(counter)
        main_page = MainPage(driver)
        main_page.click_button_constructor()
        main_page.make_order()
        list_order_page.click_button_list_orders()
        list_order_page.waiting_url_list_order()
        list_order_page.wait_card_order_to_be_clicable()
        counter_after_order = list_order_page.get_quantity_of_orders(counter)
        assert counter_before_order < counter_after_order

    @allure.title('Проверка появления нового заказа в разделе "В работе"')
    @allure.description('Проверяем, что созданный авторизованным при помощи фикстуры пользователем заказа, \
                        отображается в разделе "В работе" Ленты заказов')
    def test_new_order_is_displayed_in_progress_successful(self, driver, login_user):
        main_page = MainPage(driver)
        list_order_page = ListOrdersPage(driver)
        order_id = main_page.make_order()
        list_order_page.click_button_list_orders()
        list_order_page.waiting_url_list_order()
        list_order_page.wait_card_order_to_be_clicable()
        list_order_page.wait_order_number_in_progress()

        assert list_order_page.get_order_number_in_progress() == '0'+order_id
