from pages.base_page import BasePage
from locators.locators_personal_account_page import LocatorsPersonalAccountPage as loc_personal_account
import allure


class PersonalAccountPage(BasePage):

    @allure.step('Кликнуть на кнопку "Личный кабинет"')
    def click_button_personal_account(self):
        self.click_on_button(loc_personal_account.BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Подождать появления подождать появления "/account/profile" в url страницы')
    def waiting_url_profile(self):
        substring = '/account/profile'
        self.waiting_url_contains(substring)

    @allure.step('Получить адрес текущей страницы"')
    def get_current_page_url(self):
        return self.get_current_url()

    @allure.step('Кликнуть на кнопку "История заказов"')
    def click_button_order_history(self):
        self.click_on_element(loc_personal_account.BUTTON_ORDER_HISTORY)

    @allure.step('Кликнуть на кнопку "Выход"')
    def click_button_exit(self):
        self.click_on_element(loc_personal_account.BUTTON_EXIT)

    @allure.step('Подождать появления подождать появления "/login" в url страницы')
    def waiting_url_login(self):
        substring = 'login'
        self.waiting_url_contains(substring)

    @allure.step('Ввести email в поле ввода "Email"')
    def input_email_in_field_email_in_auth_form(self, email):
        self.waiting_for_element_to_appear(loc_personal_account.FIELD_EMAIL_AUTH_FORM)
        self.text_input_field(loc_personal_account.FIELD_EMAIL_AUTH_FORM, email)

    @allure.step('Ввести пароль в поле ввода "Пароль"')
    def input_password_in_field_password_in_auth_form(self, password):
        self.waiting_for_element_to_appear(loc_personal_account.FIELD_PASSWORD_AUTH_FORM)
        self.text_input_field(loc_personal_account.FIELD_PASSWORD_AUTH_FORM, password)

    @allure.step('Нажать на кнопку "Войти"')
    def click_button_login_in_auth_form(self):
        self.click_on_element(loc_personal_account.LOGIN_BUTTON_AUTH_FORM)

    @allure.step('Получить номер заказа в "История заказов"')
    def get_order_number(self):
        self.waiting_for_element_to_appear(loc_personal_account.ORDER_NUMBER)
        return self.get_text_of_element(loc_personal_account.ORDER_NUMBER)

    @allure.step('Узнать статус заказа')
    def get_order_status(self):
        return self.get_text_of_element(loc_personal_account.ORDER_STATUS)
