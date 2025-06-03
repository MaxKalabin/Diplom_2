import allure
import pytest
from helpers import edit_user
from test_data import STATUS_CODE_OK, STATUS_CODE_UNAUTHORIZED, UNAUTHORIZED_MESSAGE, USER, MESSAGE, NEW_DATA, EDIT_DATA

@allure.feature("Изменение данных пользователя")
class TestEditUser:

    @allure.title("Успешное обновление данных пользователя с авторизацией - возвращается ожидаемый статус 200")
    @pytest.mark.parametrize("data_field", EDIT_DATA)
    def test_update_user_with_auth_status_200(self, data_field, create_user_fixture):
        user_data, _, token = create_user_fixture
        response = edit_user({data_field: NEW_DATA}, token)
        assert response.status_code == STATUS_CODE_OK

    @allure.title("Успешное обновление данных пользователя с авторизацией - данные действительно обновились")
    @pytest.mark.parametrize("data_field", EDIT_DATA)
    def test_update_user_with_auth_has_new_data(self, data_field, create_user_fixture):
        user_data, _, token = create_user_fixture
        response = edit_user({data_field: NEW_DATA}, token)
        assert response.json()[USER][data_field] == NEW_DATA

    @allure.title("Неуспешное обновление данных пользователя без авторизации - возвращается ожидаемый статус 401")
    @pytest.mark.parametrize("data_field", EDIT_DATA)
    def test_update_user_without_auth_status_401(self, data_field):
        response = edit_user({data_field: NEW_DATA})
        assert response.status_code == STATUS_CODE_UNAUTHORIZED

    @allure.title("Неуспешное обновление данных пользователя без авторизации - возвращается сообщение о не авторизированном сообщении")
    @pytest.mark.parametrize("data_field", EDIT_DATA)
    def test_update_user_without_auth_message(self, data_field):
        response = edit_user({data_field: NEW_DATA})
        assert response.json()[MESSAGE] == UNAUTHORIZED_MESSAGE
