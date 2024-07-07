from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Найти элемент')
    def find_element(self, test_locator):
        return self.driver.find_element(*test_locator)

    def find_all_elements(self, test_locator):
        WebDriverWait(self.driver, 30, poll_frequency=10.0).until(EC.presence_of_element_located(test_locator))
        return self.driver.find_elements(*test_locator)

    @allure.step('Кликнуть на элемент')
    def click_on_element(self, test_locator):
        self.driver.find_element(*test_locator).click()

    @allure.step('Подождать появления элемента')
    def waiting_for_element_to_appear(self, test_locator):
        WebDriverWait(self.driver, 30, poll_frequency=10.0).until(EC.visibility_of_element_located(test_locator))

    def element_is_present(self, test_locator):
        WebDriverWait(self.driver, 30, poll_frequency=10.0).until(EC.presence_of_element_located(test_locator))

    @allure.step('Подождать исчезновения элемента')
    def waiting_for_element_to_disappear(self, test_locator):
        WebDriverWait(self.driver, 30, poll_frequency=10.0).until_not(EC.visibility_of_element_located(test_locator))

    @allure.step('Кликнуть по кнопке')
    def click_on_button(self, test_locator):
        target = self.driver.find_element(*test_locator)
        click = ActionChains(self.driver)
        click.move_to_element(target).click().perform()

    @allure.step('Подождать появления элемента')
    def waiting_for_all_elements_to_appear(self, test_locator):
        WebDriverWait(self.driver, 30, poll_frequency=10.0).until(EC.visibility_of_all_elements_located(test_locator))

    @allure.step('Подождать появления в URL подстроки')
    def waiting_url_contains(self, substring):
        WebDriverWait(self.driver, 20).until(EC.url_contains(substring))

    @allure.step('Проверить видимость элемента')
    def if_element_is_displayed(self, test_locator):
        return self.driver.find_element(*test_locator).is_displayed()

    @allure.step('Подождать когда элемент будет кликабелен')
    def wait_element_to_be_clicable(self, test_locator):
        return WebDriverWait(self.driver, 30, poll_frequency=10.0).until(EC.element_to_be_clickable(test_locator))

    @allure.step('Проскроллить до элемента')
    def scroll_to_element(self, test_locator):
        element = self.driver.find_element(*test_locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Ввести текст в поле')
    def text_input_field(self, test_locator, text):
        self.driver.find_element(*test_locator).send_keys(text)

    @allure.step('Получить текст элемента')
    def get_text_of_element(self, test_locator):
        return self.driver.find_element(*test_locator).text

    @allure.step('Вставить текст {text}')
    def set_text_into_element(self, test_locator, text):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(test_locator))
        self.driver.find_element(*test_locator).send_keys(text)

    @allure.step('Перетащить элемент')
    def drag_and_drop_element(self, test_locator_one, test_locator_two):
        draggable = self.driver.find_element(*test_locator_one)
        droppable = self.driver.find_element(*test_locator_two)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(draggable, droppable).perform()

    @allure.step('Открыть ссылку')
    def go_to_url(self, url):
        return self.driver.get(url)

    @allure.step('Получить текущий url')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Переключиться на другую вкладку браузера')
    def go_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Подождать изменение текста элемента')
    def wait_text_element_to_change(self, test_locator, value):
        return WebDriverWait(self.driver, 10).until_not(EC.text_to_be_present_in_element(test_locator, value))
