import allure
import pytest
from test_data import NAME, ORDER, NUMBER, MESSAGE, SUCCESS, INGREDIENTS_ERRORS
from util.data_generator import generate_valid_hash_ingredients
from util.helpers import create_order, parse_json


@allure.feature("Создание заказа")
class TestOrderCreation:

    @allure.title("Успешное создание заказа с авторизацией")
    def test_create_order_with_auth_success(self, create_user_fixture):
        _, _, token = create_user_fixture
        response = create_order(generate_valid_hash_ingredients(), token)

        with allure.step("Проверка статус-кода 200"):
            assert response.status_code == 200, f"Ожидался статус 200, получено {response.status_code}"

        json_response = response.json()
        with allure.step("Проверка поля 'success' в ответе"):
            assert SUCCESS in json_response, f"Поле '{SUCCESS}' отсутствует в ответе"
            assert json_response[SUCCESS] is True, f"Поле '{SUCCESS}' должно быть True"

        with allure.step("Проверка наличия ключей 'name', 'order' и 'number' в ответе"):
            assert NAME in json_response, "Поле 'name' отсутствует в ответе"
            assert ORDER in json_response, "Поле 'order' отсутствует в ответе"
            assert NUMBER in json_response["order"], "Поле 'number' отсутствует в 'order'"

    @allure.title("Создание заказа с авторизацией и списком ингредиентов: {ingredients}. ОР: возвращается статус {expected_status}, сообщение содержит'{expected_message}'")
    @pytest.mark.parametrize("ingredients,expected_status,expected_message,expected_success", INGREDIENTS_ERRORS)
    def test_create_order_with_auth_errors(self, create_user_fixture, ingredients, expected_status, expected_message, expected_success):
        _, _, token = create_user_fixture
        response = create_order(ingredients, token)

        with allure.step(f"Проверка статус-кода {expected_status}"):
            assert response.status_code == expected_status, \
                f"Ожидался {expected_status}, получено {response.status_code}"

        json_response = parse_json(response)
        with allure.step("Проверка поля 'success' в ответе"):
            assert json_response.get(MESSAGE) == expected_message, \
                f"Ожидалось '{expected_success}', получено '{json_response.get(SUCCESS)}'"

        with allure.step(f"Проверка сообщения об ошибке '{expected_message}'"):
            assert json_response.get(MESSAGE) == expected_message, \
                f"Ожидалось '{expected_message}', получено '{json_response.get("message") == expected_message}'"


    @allure.title("Успешное создание заказа без авторизации")
    def test_create_order_without_auth(self):
        response = create_order(generate_valid_hash_ingredients())

        with allure.step("Проверка статус-кода 200"):
            assert response.status_code == 200, f"Ожидался статус 200, получено {response.status_code}"

        json_response = response.json()
        with allure.step("Проверка поля 'success' в ответе"):
            assert SUCCESS in json_response, f"Поле '{SUCCESS}' отсутствует в ответе"
            assert json_response[SUCCESS] is True, f"Поле '{SUCCESS}' должно быть True"

        with allure.step("Проверка наличия ключей 'name', 'order' и 'number' в ответе"):
            assert NAME in json_response, f"Поле {NAME} отсутствует в ответе"
            assert ORDER in json_response, f"Поле {ORDER} отсутствует в ответе"
            assert NUMBER in json_response["order"], f"Поле {NUMBER} отсутствует в 'order'"

    @allure.title("Создание заказа с авторизацией и списком ингредиентов: {ingredients}. ОР: возвращается статус {expected_status}, сообщение содержит'{expected_message}'")
    @pytest.mark.parametrize("ingredients,expected_status,expected_message,expected_success", INGREDIENTS_ERRORS)
    def test_create_order_without_auth_errors(self, create_user_fixture, ingredients, expected_status, expected_message, expected_success):
        _, _, token = create_user_fixture
        response = create_order(ingredients)

        with allure.step(f"Проверка статус-кода {expected_status}"):
            assert response.status_code == expected_status, \
                f"Ожидался {expected_status}, получено {response.status_code}"

        json_response = parse_json(response)
        with allure.step("Проверка поля 'success' в ответе"):
            assert json_response.get(SUCCESS) is expected_success, \
                f"Ожидалось '{expected_success}', получено '{json_response.get(SUCCESS)}'"

        with allure.step(f"Проверка сообщения об ошибке '{expected_message}'"):
            assert json_response.get(MESSAGE) == expected_message, \
                f"Ожидалось '{expected_message}', получено '{json_response.get(MESSAGE) == expected_message}'"