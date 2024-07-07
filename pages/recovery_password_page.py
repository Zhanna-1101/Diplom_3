from pages.base_page import BasePage
from locators.locators_recovery_password_page import LocatorsRecoveryPasswordPage as loc_recovery_password
from helpers import TestCreatorData as data
import allure


class RecoveryPasswordPage(BasePage):

    @allure.step('Нажать кнопку "Войти в аккаунт"')
    def click_button_login(self):
        self.waiting_for_element_to_appear(loc_recovery_password.BUTTON_LOGIN_PROFILE)
        self.click_on_element(loc_recovery_password.BUTTON_LOGIN_PROFILE)

    @allure.step('Кликнуть на кнопку "Восстановить пароль"')
    def click_button_recovery_password(self):
        self.click_on_element(loc_recovery_password.BUTTON_RECOVER_PASSWORD)

    @allure.step('Получить адрес текущей страницы')
    def get_current_page_url(self):
        return self.get_current_url()

    @allure.step('Ввести email в поле ввода "Email"')
    def input_email_in_field_email(self):
        self.wait_element_to_be_clicable(loc_recovery_password.FIELD_EMAIL)
        self.text_input_field(loc_recovery_password.FIELD_EMAIL, data.data_user_full()['email'])

    @allure.step('Кликнуть на кнопку "Восстановить"')
    def click_button_recover(self):
        self.waiting_for_element_to_appear(loc_recovery_password.FIELD_EMAIL)
        self.click_on_element(loc_recovery_password.BUTTON_RECOVER)

    @allure.step('Проверить появление поля "Пароль"')
    def field_new_password_is_appeared(self):
        self.waiting_for_element_to_appear(loc_recovery_password.FIELD_FOR_NEW_PASSWORD)

    @allure.step('Ввести пароль в поле ввода "Пароль"')
    def input_password_in_field_password(self):
        self.wait_element_to_be_clicable(loc_recovery_password.FIELD_FOR_NEW_PASSWORD)
        self.text_input_field(loc_recovery_password.FIELD_FOR_NEW_PASSWORD, data.data_user_full()['password'])

    @allure.step('Нажать на иконку глаза, чтобы увидеть пароль"')
    def click_to_show_password(self):
        self.wait_element_to_be_clicable(loc_recovery_password.ICON_SHOW_PASSWORD)
        self.click_on_button(loc_recovery_password.ICON_SHOW_PASSWORD)

    @allure.step('Убедиться, что поле ввода пароля активно')
    def check_input_password_field(self):
        return self.find_element(loc_recovery_password.FIELD_PASSWORD_ACTIVE)
