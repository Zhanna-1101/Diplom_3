from pages.personal_account_page import PersonalAccountPage
from data_static import Urls as url
import allure


class TestPersonalAccountPage:

    @allure.title('Проверка перехода в профиль по клику на "Личный кабинет"')
    @allure.description('Проверяем переход ранее авторизованного, при помощи фикстуры, пользователя в Личный кабинет по \
                        клику на кнопку "Линый кабинет" на главной странице')
    def test_switch_to_personal_account_successful(self, driver, login_user):
        account_page = PersonalAccountPage(driver)
        account_page.click_button_personal_account()
        account_page.waiting_url_profile()
        assert account_page.get_current_page_url() == url.PROFILE_PAGE

    @allure.title('Проверка перехода по клику на "История заказов"')
    @allure.description('Проверяем возможность перемещения ранее авторизованного, при помощи фикстуры, пользователя \
                        в Личном кабинете с открываемой по умолчанию вкладки "Профиль" на вкладку "История заказов"')
    def test_switch_to_order_history_tab__in_oersonal_account_successful(self, driver, login_user):
        account_page = PersonalAccountPage(driver)
        account_page.click_button_personal_account()
        account_page.waiting_url_profile()
        account_page.click_button_order_history()
        assert account_page.get_current_page_url() == url.ORDERS_HISTORY

    @allure.title('Проверка выполнения логаута по кнопке "Выйти"')
    @allure.description('Проверяем выход ранее авторизованного, при помощи фикстуры, пользователя из Личного кабинета \
                        по нажатию на кнопку "Выйти" в Личном кабинете')
    def test_logout_from_personal_account_successful(self, driver, login_user):
        account_page = PersonalAccountPage(driver)
        account_page.click_button_personal_account()
        account_page.waiting_url_profile()
        account_page.click_button_exit()
        account_page.waiting_url_login()
        assert account_page.get_current_page_url() == url.LOGIN_PAGE
