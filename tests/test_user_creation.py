import allure
import pytest
from test_data import STATUS_CODE_OK, STATUS_CODE_FORBIDDEN, SUCCESS, MESSAGE, USER_ALREADY_EXISTS, USER_DATA, \
    REQUIRED_FIELDS_MESSAGE, EMAIL, NAME, ACCESS_TOKEN, REFRESH_TOKEN, USER
from util.helpers import create_user, parse_json


@allure.feature("Создание пользователя")
class TestUserCreation:

    @allure.title("Успешное создание уникального нового пользователя. ОР: статус 200 и success: True, токенов и содержимого 'user'")
    def test_create_unique_user(self, create_user_fixture):
        _, response, _ = create_user_fixture

        with allure.step("Проверка статус-кода 200"):
            assert response.status_code == STATUS_CODE_OK, \
                f"Ожидался {STATUS_CODE_OK}, получено {response.status_code}"

        json_response = parse_json(response)
        with allure.step("Проверка поля 'success' в ответе"):
            assert SUCCESS in json_response, \
                f"Поле '{SUCCESS}' отсутствует в ответе"
            assert json_response[SUCCESS] is True, \
                f"Поле '{SUCCESS}' должно быть True"

        with allure.step("Проверка наличия поля 'user' и его содержимого"):
            assert USER in json_response, "Поле 'user' отсутствует в ответе"
            user = json_response[USER]
            assert EMAIL in user, f"Поле '{EMAIL}' отсутствует в 'user'"
            assert NAME in user, f"Поле '{NAME}' отсутствует в 'user'"

        with allure.step("Проверка наличия токенов"):
            assert ACCESS_TOKEN in json_response, \
                f"Поле '{ACCESS_TOKEN}' отсутствует в ответе"
            assert REFRESH_TOKEN in json_response, \
                f"Поле '{REFRESH_TOKEN}' отсутствует в ответе"

    @allure.title("Неуспешное создание существующего пользователя. ОР: статус 403 и сообщение 'User already exists'")
    def test_create_existing_user(self, create_user_fixture):
        user_data, _, _ = create_user_fixture
        response = create_user(user_data)
        with allure.step(f"Проверка статус-кода {STATUS_CODE_FORBIDDEN}"):
            assert response.status_code == STATUS_CODE_FORBIDDEN, \
                f"Ожидался {STATUS_CODE_FORBIDDEN}, получено {response.status_code}"

        with allure.step(f"Проверка сообщения об ошибке '{USER_ALREADY_EXISTS}'"):
            json_response = parse_json(response)
            assert MESSAGE in json_response, \
                f"Поле '{MESSAGE}' отсутствует в ответе"
            assert json_response[MESSAGE] == USER_ALREADY_EXISTS, \
                f"Ожидалось сообщение '{USER_ALREADY_EXISTS}', получено '{json_response[MESSAGE]}'"

    @allure.title("Неуспешное создание пользователя без обязательного поля: {missing_field}. ОР: статус 403 и сообщение '{REQUIRED_FIELDS_MESSAGE}'")
    @pytest.mark.parametrize("missing_field", USER_DATA)
    def test_create_missing_required_field_message(self, missing_field, generate_user_data):
        del generate_user_data[missing_field]
        response = create_user(generate_user_data)

        with allure.step(f"Проверка статус-кода {STATUS_CODE_FORBIDDEN}"):
            assert response.status_code == STATUS_CODE_FORBIDDEN, \
                f"Ожидался {STATUS_CODE_FORBIDDEN}, получено {response.status_code}"

        with allure.step(f"Проверка сообщения об ошибке '{REQUIRED_FIELDS_MESSAGE}'"):
            json_response = parse_json(response)
            assert MESSAGE in json_response, \
                f"Поле '{MESSAGE}' отсутствует в ответе"
            assert json_response[MESSAGE] == REQUIRED_FIELDS_MESSAGE, \
                f"Ожидалось сообщение '{REQUIRED_FIELDS_MESSAGE}', получено '{json_response[MESSAGE]}'"
