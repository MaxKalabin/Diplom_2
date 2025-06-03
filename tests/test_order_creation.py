import allure
import pytest
from helpers import create_order, generate_valid_hash_ingredients
from test_data import STATUS_CODE_OK, STATUS_CODE_BAD_REQUEST, \
    INVALID_INGREDIENT_HASH, STATUS_CODE_INTERNAL_SERVER_ERROR

INGREDIENTS_DATA = [
    (generate_valid_hash_ingredients(), STATUS_CODE_OK),
    ([], STATUS_CODE_BAD_REQUEST),
    ([INVALID_INGREDIENT_HASH], STATUS_CODE_INTERNAL_SERVER_ERROR)
]

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
