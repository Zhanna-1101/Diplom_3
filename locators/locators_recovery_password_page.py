from selenium.webdriver.common.by import By


class LocatorsRecoveryPasswordPage:

    # Кнопка "Войти в аккаунт" на главной странице
    BUTTON_LOGIN_PROFILE = By.XPATH, "//button[text()='Войти в аккаунт']"

    # Кнопка "Восстановить пароль" на странице авторизации
    BUTTON_RECOVER_PASSWORD = By.XPATH, "//a[.='Восстановить пароль']"

    # Поле ввода "Email" на странице восстановления пароля
    FIELD_EMAIL = By.XPATH, ".//input[@name = 'name']"

    # Кнопка "Восстановить" на странице восстановления пароля
    BUTTON_RECOVER = By.XPATH, "//button[text()='Восстановить']"

    # Поле ввода "Пароль" на странице восстановления пароля
    FIELD_FOR_NEW_PASSWORD = By.XPATH, ".//input[@name = 'Введите новый пароль']"

    # Иконка "Показать пароль" на странице восстановления пароля
    ICON_SHOW_PASSWORD = By.CSS_SELECTOR, '.input__icon'

    # Поле ввода "Пароль" активное
    FIELD_PASSWORD_ACTIVE = By.CSS_SELECTOR, '.input.input_status_active'
