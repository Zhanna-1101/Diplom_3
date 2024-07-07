import random
import requests
from faker import Faker
from data_static import EndPoints as ep


class TestCreatorData:

    # Создаем полный нвбор тестовых данных для регистрации пользователя
    @staticmethod
    def data_user_full():
        data_user = {
            'email': Faker().company_email(),
            'password': Faker().password(),
            'name': Faker(locale='ru_RU').first_name()}
        return data_user

    # Создаем корректный набор тестовых данных для создания заказа
    @staticmethod
    def set_ingredients_with_correct_hash():
        ingredients = []
        response = requests.get(ep.GET_INGREDIENTS)
        list = response.json()['data']
        for i in list:
            ingredients.append(i.get('_id'))
        last_index = len(ingredients) - 1
        first_ingredient = ingredients[random.randint(0, last_index)]
        second_ingredient = ingredients[random.randint(0, last_index)]
        correct_set = {"ingredients": [first_ingredient, second_ingredient]}
        return correct_set
