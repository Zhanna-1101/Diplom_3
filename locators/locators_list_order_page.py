from selenium.webdriver.common.by import By


class LocatorsListOrderPage:

    # Кнопка "Лента заказов" на главной странице
    BUTTON_LIST_ORDERS = By.XPATH, ".//p[contains(text(), 'Лента Заказов')]"

    # Заголовок Ленты заказов
    TITLE_LIST_ORDERS = By.XPATH, '//h1[text()="Лента заказов"]'

    # Ссылка на заказ в списке "Лента заказа"
    LINK_ORDER = By.XPATH, '//*[contains(@class, "OrderHistory_link")]'

    # Все заказы сделанные пользователями в Ленте заказов
    ALL_ORDERS = By.XPATH, './/p[contains(@class, "text_type_digits-default")]'

    # Количество заказов пользователей выполненных за сегодня
    COMPLETED_ORDERS_TODAY = By.XPATH, ('//p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class,'
                                        '"digits-large")]')

    # Количество заказов пользователей выполненных за всё время
    COMPLETED_ORDERS_ALL_TIME = By.XPATH, ('//p[text()="Выполнено за все время:"]/following-sibling::p[contains(@class,'
                                        '"digits-large")]')

    # Счетчик заказов "В работе" на страницы Ленты заказов
    ORDER_IN_WORK = By.XPATH, '//*[contains(@class,"orderListReady")]//li[contains(@class,"digits-default")]'

    # Текст "Все текущие заказы готовы!"
    ORDERS_READY_TEXT = By.XPATH, '//li[text()="Все текущие заказы готовы!"]'

    # Заголовок "Состав" в окне с деталями заказа
    ORDER_COMPOSITION = By.XPATH, '//p[text()="Cостав"]'

    # Статус заказа "Выполнен"
    ORDER_COMPLETED = By.XPATH, '//p[text()="Выполнен"]'

    # Номер заказа из списка "Лента заказов"
    ORDER_NUMBER_IN_LIST_ORDERS = By.XPATH, '//p[text()="{}"]'

    # Номер заказа "В работе" в Ленте заказов
    ORDER_IF_IN_PROGRESS = By.XPATH, '//*[contains(@class,"orderListReady")]//li[contains(@class,"digits-default")]'
