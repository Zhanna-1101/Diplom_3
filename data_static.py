class Urls:

    MAIN_PAGE_URL = 'https://stellarburgers.nomoreparties.site'
    LOGIN_PAGE = f'{MAIN_PAGE_URL}/login'
    PROFILE_PAGE = f'{MAIN_PAGE_URL}/account/profile'
    RECOVERY_PASSWORD_PAGE = f'{MAIN_PAGE_URL}/forgot-password'
    RESET_PASSWORD_PAGE = f'{MAIN_PAGE_URL}/reset-password'
    ORDERS_HISTORY = f'{MAIN_PAGE_URL}/account/order-history'
    LIST_PAGE_URL = f'{MAIN_PAGE_URL}/feed'


class EndPoints:

    CREATE_USER = f'{Urls.MAIN_PAGE_URL}/api/auth/register'
    LOGIN_USER = f'{Urls.MAIN_PAGE_URL}/api/auth/login'
    DELETE_USER = f'{Urls.MAIN_PAGE_URL}/api/auth/user'
    CREATE_ORDER = f'{Urls.MAIN_PAGE_URL}/api/orders'
    GET_INGREDIENTS = f'{Urls.MAIN_PAGE_URL}/api/ingredients'
