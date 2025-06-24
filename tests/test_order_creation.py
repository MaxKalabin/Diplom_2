import allure
import pytest

from util.data_generator import INGREDIENTS_DATA
from util.helpers import create_order


@allure.feature("Создание заказа")
class TestOrderCreation:

    @allure.title("Создание заказа с авторизацией и списком ингредиентов: {ingredients} - возвращается ожидаемый статус: {expected_status}")
    @pytest.mark.parametrize("ingredients,expected_status", INGREDIENTS_DATA)
    def test_create_order_with_auth(self, create_user_fixture, ingredients, expected_status):
        _, _, token = create_user_fixture
        response = create_order(ingredients, token)
        assert response.status_code == expected_status

    @allure.title("Создание заказа без авторизации и списком ингредиентов: {ingredients} - возвращается ожидаемый статус: {expected_status}")
    @pytest.mark.parametrize("ingredients,expected_status", INGREDIENTS_DATA)
    def test_create_order_without_auth(self, ingredients, expected_status):
        response = create_order(ingredients)
        assert response.status_code == expected_status
