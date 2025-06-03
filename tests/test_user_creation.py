import allure
import pytest
from helpers import create_user
from test_data import STATUS_CODE_OK, SUCCESS, STATUS_CODE_FORBIDDEN, MESSAGE, USER_ALREADY_EXISTS, USER_DATA, \
    REQUIRED_FIELDS_MESSAGE

@allure.feature("Создание пользователя")
class TestUserCreation:

    @allure.title("Успешное создание уникального нового пользователя")
    def test_create_unique_user(self, create_user_fixture):
        _, response, _ = create_user_fixture
        assert response.status_code == STATUS_CODE_OK

    @allure.title("Успешное создание уникального пользователя - тело ответа содержит success: True")
    def test_create_unique_user_success_flag(self, create_user_fixture):
        _, response, _ = create_user_fixture
        assert response.json()[SUCCESS] is True

    @allure.title("Неуспешное создание существующего пользователя - возвращается ожидаемый статус 403")
    def test_create_existing_user(self, create_user_fixture):
        user_data, _, _ = create_user_fixture
        response = create_user(user_data)
        assert response.status_code == STATUS_CODE_FORBIDDEN

    @allure.title("Неуспешное создание существующего пользователя - тело ответа содержит ожидаемое сообщение")
    def test_create_existing_user_message(self, create_user_fixture):
        user_data, _, _ = create_user_fixture
        response = create_user(user_data)
        assert response.json()[MESSAGE] == USER_ALREADY_EXISTS

    @allure.title("Неуспешное создание пользователя без обязательного поля - возвращается ожидаемый статус 403")
    @pytest.mark.parametrize("missing_field", USER_DATA)
    def test_create_missing_required_field_status(self, missing_field, generate_user_data):
        del generate_user_data[missing_field]
        response = create_user(generate_user_data)
        assert response.status_code == STATUS_CODE_FORBIDDEN

    @allure.title("Неуспешное создание пользователя без обязательного поля - возвращается ожидаемое сообщение")
    @pytest.mark.parametrize("missing_field", USER_DATA)
    def test_create_missing_required_field_message(self, missing_field, generate_user_data):
        del generate_user_data[missing_field]
        response = create_user(generate_user_data)
        assert response.json()[MESSAGE] == REQUIRED_FIELDS_MESSAGE
