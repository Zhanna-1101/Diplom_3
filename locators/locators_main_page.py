from selenium.webdriver.common.by import By


class LocatorsMainPage:

    # Кнопка "Конструктор" на главной странице
    BUTTON_CONSTRUCTOR = By.XPATH, ".//p[contains(text(), 'Конструктор')]"

    # Кнопка "Лента заказов" на главной странице
    BUTTON_LIST_ORDER = By.XPATH, ".//p[contains(text(), 'Лента Заказов')]"

    # Кнопка "Оформить заказ" на главной странице
    BUTTON_MAKE_ORDER = By.XPATH, "//button[text()='Оформить заказ']"

    # Заголовок раздела "Конструктор" на главной странице
    TITLE_CONSTRUCTOR_ORDER = By.XPATH, "//section[contains(@class, 'BurgerIngredients_ingredients')]/h1"

    # Ингредиент "Флюоресцентная булка R2-D3 на главной странице
    BUTTON_INGREDIENT_BUN = By.XPATH, ".//img[@alt = 'Флюоресцентная булка R2-D3']"

    # Всплывающее окно с информацией об ингредиенте
    WINDOW_INGREDIENT_DETAILS = By.XPATH, "//*[contains(@class, 'contentBox')]"

    # Заголовок всплывающего окна с информацией об ингредиенте
    TITLE_WINDOW_INGREDIENT_DETAILS = By.XPATH, "//h2[text()='Детали ингредиента']"

    # Кнопка закрытия всплевающего окна с информацией об ингредиенте
    BUTTON_CLOSING_WINDOW_DETAILS_INGREDIENT = By.XPATH, "//button[contains(@class,'close')]"

    # Счетчик ингредиента в "корзине"
    COUNTER_INGREDIENT = By.XPATH, '//ul[1]/a[1]//p[contains(@class, "num")]'

    # Корзина, куда переносятся ингредиенты
    BASKET_ORDER = By.XPATH, "//span[@class='constructor-element__text' and text()='Перетяните булочку сюда (низ)']"

    # Текст статуса заказа: "Ваш заказ начали готовить"
    TEXT_ORDER_STATUS = By.XPATH, "//p[text()='Ваш заказ начали готовить']"

    # Окно подтверждения создания заказа
    WINDOW_CONFIRMATION_ORDER = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]/div[contains'
                                             '(@class, "Modal_modal__container")]')

    # Номер заказа в окне подтверждения заказа
    NUMBER_OF_ORDER_IN_WINDOW_CONFIRMATION = By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//h2'

    # Кнопка с крестиком, закрывающая окно подтвержденного заказа
    BUTTON_CLOSING_WINDOW_CONFIRMATION = By.XPATH, '//section[contains(@class, "Modal_modal_opened")'']//button[contains(@class, "close")]'
