import allure
import pytest
from util.data_generator import INGREDIENTS_DATA
from util.helpers import create_order, parse_json


@allure.feature("Создание заказа")
class TestOrderCreation:

    @allure.title("Создание заказа с авторизацией и списком ингредиентов: {ingredients} - возвращается ожидаемый статус: {expected_status}")
    @pytest.mark.parametrize("ingredients,expected_status,expected_message,expected_success", INGREDIENTS_DATA)
    def test_create_order_with_auth_has_expected_status(self, create_user_fixture, ingredients, expected_status, expected_message, expected_success):
        _, _, token = create_user_fixture
        response = create_order(ingredients, token)
        assert response.status_code == expected_status

    @allure.title("Создание заказа с авторизацией и списком ингредиентов: {ingredients} - возвращается статус {expected_status}, сообщение содержит'{expected_message}'")
    @pytest.mark.parametrize("ingredients,expected_status,expected_message,expected_success", INGREDIENTS_DATA)
    def test_create_order_with_auth_has_expected_content(self, create_user_fixture, ingredients, expected_status, expected_message, expected_success):
        _, _, token = create_user_fixture
        response = create_order(ingredients, token)
        json_response = parse_json(response)

        if expected_success:
            assert json_response.get("success") is True
            assert "name" in json_response
            assert "order" in json_response
            assert "number" in json_response["order"]
        else:
            assert json_response.get("success") is expected_success
            assert json_response.get("message") == expected_message

    @allure.title("Создание заказа без авторизации и списком ингредиентов: {ingredients} - возвращается ожидаемый статус: {expected_status}")
    @pytest.mark.parametrize("ingredients,expected_status,expected_message,expected_success", INGREDIENTS_DATA)
    def test_create_order_without_auth_has_expected_status(self, ingredients, expected_status, expected_message, expected_success):
        response = create_order(ingredients)
        assert response.status_code == expected_status

    @allure.title("Создание заказа без авторизации и списком ингредиентов: {ingredients} - возвращается статус {expected_status}, сообщение содержит'{expected_message}'")
    @pytest.mark.parametrize("ingredients,expected_status,expected_message,expected_success", INGREDIENTS_DATA)
    def test_create_order_without_auth_has_expected_content(self, ingredients, expected_status, expected_message, expected_success):
        response = create_order(ingredients)
        json_response = parse_json(response)

        if expected_success:
            assert json_response.get("success") is True
            assert "name" in json_response
            assert "order" in json_response
            assert "number" in json_response["order"]
        else:
            assert json_response.get("success") is expected_success
            assert json_response.get("message") == expected_message