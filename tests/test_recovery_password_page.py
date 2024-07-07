from pages.recovery_password_page import RecoveryPasswordPage
from data_static import Urls as url
import allure


class TestRecoveryPasswordPage():

    @allure.title('Проверка перехода на страницу восстановления пароля при нажатии на кнопку "Восстановить пароль')
    @allure.description('Проверяем переход на страницу восстановления пароля путем нажатия кнопки "Войти в аккаунт" на главной странице и \
                        и далее кнопки "Восстановить пароль" на странице авторизации')
    def test_switch_to_recovery_password_page_successful(self, driver):
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.click_button_login()
        recovery_page.click_button_recovery_password()

        assert recovery_page.get_current_page_url() == url.RECOVERY_PASSWORD_PAGE

    @allure.title('Проверка перехода к странице назначения нового пароля при вводе email и нажатии кнопки "Восстановить"')
    @allure.description('Проверяем переход на страницу назначения нового пароля путем ввода адреса электронной почты  и нажатия кнопки \
                        "Восстановить" на странице восстановления пароля')
    def test_switch_to_reset_password_page_successful(self, driver):
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.click_button_login()
        recovery_page.click_button_recovery_password()
        recovery_page.input_email_in_field_email()
        recovery_page.click_button_recover()
        recovery_page.field_new_password_is_appeared()

        assert recovery_page.get_current_page_url() == url.RESET_PASSWORD_PAGE

    @allure.title('Проверка, что поле "Пароль" при восстановлении пароля активно')
    @allure.description('Проверяем активность поля "Пароль на странице назначения нового пароля')
    def test_show_password_by_click_icon_successful(self, driver):
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.click_button_login()
        recovery_page.click_button_recovery_password()
        recovery_page.input_email_in_field_email()
        recovery_page.click_button_recover()
        recovery_page.input_password_in_field_password()
        recovery_page.click_to_show_password()

        assert recovery_page.check_input_password_field()
