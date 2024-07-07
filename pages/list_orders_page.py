from pages.base_page import BasePage
from locators.locators_list_order_page import LocatorsListOrderPage as loc_list_order
import allure


class ListOrdersPage(BasePage):

    @allure.step('Кликнуть на кнопку "Лента заказов"')
    def click_button_list_orders(self):
        self.waiting_for_all_elements_to_appear(loc_list_order.BUTTON_LIST_ORDERS)
        self.click_on_button(loc_list_order.BUTTON_LIST_ORDERS)

    @allure.step('Подождать появления "/feed" в url страницы')
    def waiting_url_list_order(self):
        substring = '/feed'
        self.waiting_url_contains(substring)

    @allure.step('Получить адрес текущей страницы"')
    def get_current_page_url(self):
        return self.get_current_url()

    @allure.step('Получить заголовок Ленты заказов"')
    def get_title_list_order(self):
        self.waiting_for_element_to_appear(loc_list_order.TITLE_LIST_ORDERS)
        return self.get_text_of_element(loc_list_order.TITLE_LIST_ORDERS)

    @allure.step('Подождать, пока карточка заказа будет кликабельна')
    def wait_card_order_to_be_clicable(self):
        self.wait_element_to_be_clicable(loc_list_order.LINK_ORDER)

    @allure.step('Кликнуть на карточку товара"')
    def click_card_order(self):
        self.click_on_button(loc_list_order.LINK_ORDER)

    @allure.step('Проверить открытие карточки заказа в Ленте заказов"')
    def check_open_card_order_in_list_order(self):
        self.waiting_for_element_to_appear(loc_list_order.ORDER_COMPOSITION)
        return self.if_element_is_displayed(loc_list_order.ORDER_COMPOSITION)

    @allure.step('Получить количество заказов, выполненных за все время')
    def get_quantity_of_orders(self, counter):
        self.waiting_for_all_elements_to_appear(counter)
        return self.get_text_of_element(counter)

    @allure.step('Получить номер заказа, находящегося в работе')
    def get_order_number_in_progress(self):
        self.wait_text_element_to_change(loc_list_order.ORDER_IF_IN_PROGRESS, 'Все текущие заказы готовы!')
        return self.get_text_of_element(loc_list_order.ORDER_IF_IN_PROGRESS)

    def wait_order_number_in_progress(self):
        self.waiting_for_element_to_appear(loc_list_order.ORDER_IF_IN_PROGRESS)

    @allure.step('Получить текст заказа в локаторе')
    def get_locators_text(self, test_locator):
        all_locators = self.find_all_elements(test_locator)
        locator_text = []
        for order in all_locators:
            locator_text.append(order.text)
        return locator_text

    @allure.step('Получить текст всех заказов в локаторах')
    def get_numbers_all_orders(self):
        self.waiting_for_all_elements_to_appear(loc_list_order.ALL_ORDERS)
        return self.get_locators_text(loc_list_order.ALL_ORDERS)
