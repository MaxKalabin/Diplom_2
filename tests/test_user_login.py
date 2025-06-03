import allure
import pytest
from helpers import login_user
from test_data import STATUS_CODE_OK, INVALID_CREDENTIALS_MESSAGE, LOGIN_DATA, \
    STATUS_CODE_UNAUTHORIZED, ACCESS_TOKEN, MESSAGE

@allure.feature("Логин пользователя")
class TestUserLogin:

    @allure.title("Успешный логин существующего пользователя - возвращается ожидаемый статус 200")
    def test_login_existing_user_status_200(self, create_user_fixture):
        payload, _, _ = create_user_fixture
        response = login_user(payload)
        assert response.status_code == STATUS_CODE_OK

    @allure.title("Успешный логин существующего пользователя - тело ответа содержит токен")
    def test_login_existing_user_has_token(self, create_user_fixture):
        payload, _, _ = create_user_fixture
        response = login_user(payload)
        assert ACCESS_TOKEN in response.json()

    @allure.title("Неуспешный логин с неверными учетными данными - возвращается ожидаемый статус 401")
    @pytest.mark.parametrize("wrong_field", LOGIN_DATA)
    def test_login_invalid_credentials_status_401(self, wrong_field, create_user_fixture):
        valid_payload, _, _ = create_user_fixture
        invalid_payload = valid_payload.copy()
        invalid_payload[wrong_field] = "wrong_" + invalid_payload[wrong_field]
        response = login_user(invalid_payload)
        assert response.status_code == STATUS_CODE_UNAUTHORIZED

    @allure.title("Неуспешный логин с неверными учетными данными - возвращается ожидаемое сообщение")
    @pytest.mark.parametrize("wrong_field", LOGIN_DATA)
    def test_login_invalid_credentials_message(self, wrong_field, create_user_fixture):
        valid_payload, _, _ = create_user_fixture
        invalid_payload = valid_payload.copy()
        invalid_payload[wrong_field] = "wrong_" + invalid_payload[wrong_field]
        response = login_user(invalid_payload)
        assert response.json()[MESSAGE] == INVALID_CREDENTIALS_MESSAGE