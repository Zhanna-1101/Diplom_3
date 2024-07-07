from selenium.webdriver.common.by import By


class LocatorsPersonalAccountPage:

    # Кнопка "Личный кабинет" на главной странице
    BUTTON_PERSONAL_ACCOUNT = By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]"

    # История заказов
    BUTTON_ORDER_HISTORY = By.XPATH, "//a[.='История заказов']"

    # Раздел "Профиль" в личном кабинете пользователя
    BUTTON_PROFILE = By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]"

    # Кнопка "Выход" в личном кабинете пользователя
    BUTTON_EXIT = By.XPATH, "//button[@type='button' and text()='Выход']"

    # Поле "Email" на странице авторизации
    FIELD_EMAIL_AUTH_FORM = By.XPATH, "//input[@type='text' and @name='name']"

    # Поле "Пароль" на странице авторизации
    FIELD_PASSWORD_AUTH_FORM = By.XPATH, "//input[@type='password' and @name='Пароль']"

    # Кнопка "Войти" на странице авторизации
    LOGIN_BUTTON_AUTH_FORM = By.XPATH, ".//button[text()='Войти']"

    # Статус заказа в истории заказов личного кабинета пользователя
    ORDER_STATUS = By.XPATH, "//p[text()='Выполнен']"

    # Номер заказа в истории заказов личного кабинета пользователя
    ORDER_NUMBER = By.XPATH, '//*[contains(@class,"textBox")]//p[contains(@class,"digits-default")]'
