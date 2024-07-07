import pytest
import requests
from selenium import webdriver
from helpers import TestCreatorData as data
from data_static import Urls as url, EndPoints as ep
from pages.personal_account_page import PersonalAccountPage
from pages.recovery_password_page import RecoveryPasswordPage


# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get(url.MAIN_PAGE_URL)
#     yield driver
#     driver.quit()
@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
    elif request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
    driver.get(url.MAIN_PAGE_URL)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
# Создать пользователя
def create_user():
    data_user = data.data_user_full()
    response = requests.post(ep.CREATE_USER, data=data_user)
    del data_user['name']
    yield data_user, response
    token = {'Authorization': response.json()['accessToken']}
    requests.delete(ep.DELETE_USER, headers=token)


@pytest.fixture(scope='function')
# Авторизовать пользователя'
def login_user(driver, create_user):
    recovery_page = RecoveryPasswordPage(driver)
    recovery_page.click_button_login()
    account_page = PersonalAccountPage(driver)
    account_page.input_email_in_field_email_in_auth_form(create_user[0]['email'])
    account_page.input_password_in_field_password_in_auth_form(create_user[0]['password'])
    account_page.click_button_login_in_auth_form()
