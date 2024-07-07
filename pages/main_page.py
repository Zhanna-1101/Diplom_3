from pages.base_page import BasePage
from locators.locators_main_page import LocatorsMainPage as loc_main_page
import allure


class MainPage(BasePage):

    @allure.step('Подождать появления кнопки "Оформить заказ"')
    def button_make_order_is_appeared(self):
        self.waiting_for_element_to_appear(loc_main_page.BUTTON_MAKE_ORDER)

    @allure.step('Кликнуть на кнопку "Конструктор"')
    def click_button_constructor(self):
        self.waiting_for_element_to_appear(loc_main_page.BUTTON_CONSTRUCTOR)
        self.click_on_element(loc_main_page.BUTTON_CONSTRUCTOR)

    @allure.step('Получить адрес текущей страницы"')
    def get_current_page_url(self):
        return self.get_current_url()

    @allure.step('Получить текст заголовка Конструктора заказов"')
    def get_title_of_constructor_order(self):
        return self.get_text_of_element(loc_main_page.TITLE_CONSTRUCTOR_ORDER)

    @allure.step('Кликнуть на ингредиент для открытия окна "Детали ингредиента"')
    def click_ingredient_burger(self):
        self.click_on_button(loc_main_page.BUTTON_INGREDIENT_BUN)

    @allure.step('Кликнуть кнопку с крестиком окна "Детали ингредиента" для закрытия этого окна')
    def click_to_close_window_details_of_ingredient(self):
        self.waiting_for_element_to_appear(loc_main_page.BUTTON_CLOSING_WINDOW_DETAILS_INGREDIENT)
        self.click_on_element(loc_main_page.BUTTON_CLOSING_WINDOW_DETAILS_INGREDIENT)

    @allure.step('Получить заголовок окна "Детали ингредиента"')
    def get_title_of_window_details_of_ingredient(self):
        self.waiting_for_element_to_appear(loc_main_page.TITLE_WINDOW_INGREDIENT_DETAILS)
        return self.get_text_of_element(loc_main_page.TITLE_WINDOW_INGREDIENT_DETAILS)

    @allure.step('Проверка открытия окна "Детали ингредиента"')
    def check_openinng_window_details_of_ingredient(self):
        return self.if_element_is_displayed(loc_main_page.WINDOW_INGREDIENT_DETAILS)

    @allure.step('Проверка закрытия окна "Детали ингредиента"')
    def check_closing_window_details_of_ingredient(self):
        self.waiting_for_element_to_disappear(loc_main_page.WINDOW_INGREDIENT_DETAILS)
        if not self.if_element_is_displayed(loc_main_page.WINDOW_INGREDIENT_DETAILS):
            return True

    @allure.step('Добавление (перетаскивание) ингредиента в "корзину"')
    def drag_and_drop_ingredient_into_basket(self):
        self.drag_and_drop_element(loc_main_page.BUTTON_INGREDIENT_BUN, loc_main_page.BASKET_ORDER)

    @allure.step('Получение количества ингредиентов в корзине')
    def get_count_of_ingredients_into_basket(self):
        return self.get_text_of_element(loc_main_page.COUNTER_INGREDIENT)

    @allure.step('Кликнуть на кнопку создания заказа')
    def click_button_make_order(self):
        self.waiting_for_element_to_appear(loc_main_page.BUTTON_MAKE_ORDER)
        self.click_on_element(loc_main_page.BUTTON_MAKE_ORDER)

    @allure.step('Проверить отображение окна подтверждения заказа')
    def check_window_confirmation_order_is_displayed(self):
        self.waiting_for_element_to_appear(loc_main_page.WINDOW_CONFIRMATION_ORDER)
        return self.if_element_is_displayed(loc_main_page.WINDOW_CONFIRMATION_ORDER)

    @allure.step('Получить номер в окне подтвеждения заказа')
    def get_order_number_in_window_confirmation(self):
        self.wait_text_element_to_change(loc_main_page.NUMBER_OF_ORDER_IN_WINDOW_CONFIRMATION, '9999')
        return self.get_text_of_element(loc_main_page.NUMBER_OF_ORDER_IN_WINDOW_CONFIRMATION)

    @allure.step('Получить текст в окне подтвеждения заказа')
    def get_order_status_in_window_confirmation(self):
        self.waiting_for_element_to_appear(loc_main_page.TEXT_ORDER_STATUS)
        return self.get_text_of_element(loc_main_page.TEXT_ORDER_STATUS)

    @allure.step('Кликнуть на кнопку закрытия окна подтверждения заказа')
    def click_button_to_close_window_confirmation(self):
        self.waiting_for_element_to_appear(loc_main_page.WINDOW_CONFIRMATION_ORDER)
        self.click_on_button(loc_main_page.BUTTON_CLOSING_WINDOW_CONFIRMATION)

    @allure.step('Создать заказ на сайте через Конструктор')
    def make_order(self):
        self.waiting_for_all_elements_to_appear(loc_main_page.BUTTON_MAKE_ORDER)
        self.drag_and_drop_element(loc_main_page.BUTTON_INGREDIENT_BUN, loc_main_page.BASKET_ORDER)
        self.waiting_for_element_to_appear(loc_main_page.BUTTON_MAKE_ORDER)
        self.click_on_button(loc_main_page.BUTTON_MAKE_ORDER)
        self.waiting_for_element_to_appear(loc_main_page.WINDOW_CONFIRMATION_ORDER)
        order_id = self.get_order_number_in_window_confirmation()
        self.click_on_button(loc_main_page.BUTTON_CLOSING_WINDOW_CONFIRMATION)
        return order_id
