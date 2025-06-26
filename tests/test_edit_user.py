import allure
import pytest
from util.helpers import edit_user
from test_data import STATUS_CODE_OK, STATUS_CODE_UNAUTHORIZED, UNAUTHORIZED_MESSAGE, USER, MESSAGE, NEW_DATA, \
    EDIT_DATA, SUCCESS


@allure.feature("Изменение данных пользователя")
class TestEditUser:

    @allure.title("Успешное обновление данных пользователя с авторизацией. ОР: статус 200, success: True и наличие данных 'USER'")
    @pytest.mark.parametrize("data_field", EDIT_DATA)
    def test_update_user_with_auth(self, data_field, create_user_fixture):
        user_data, _, token = create_user_fixture
        response = edit_user({data_field: NEW_DATA}, token)

        with allure.step(f"Проверка статус-кода при обновлении поля {data_field}"):
            assert response.status_code == STATUS_CODE_OK, \
                f"Ожидаемый статус-код: {STATUS_CODE_OK}, полученный: {response.status_code}"

        json_response = response.json()
        with allure.step("Проверка поля 'success' в ответе"):
            assert SUCCESS in json_response, \
                f"Поле '{SUCCESS}' отсутствует в ответе"
            assert json_response[SUCCESS] is True, \
                f"Поле '{SUCCESS}' должно быть True"

        with allure.step(f"Проверка обновления поля {data_field}"):
            assert USER in json_response, f"Поле '{USER}' отсутствует в ответе"
            assert json_response[USER][data_field] == NEW_DATA, \
                f"Поле {data_field} не обновилось. Ожидалось: {NEW_DATA}, \
                получено: {json_response[USER][data_field]}"

    @allure.title("Неуспешное обновление данных пользователя без авторизации. ОР: статус 401, success: False и сообщение об ошибке")
    @pytest.mark.parametrize("data_field", EDIT_DATA)
    def test_update_user_without_auth(self, data_field):
        response = edit_user({data_field: NEW_DATA})

        with allure.step(f"Проверка статус-кода при попытке обновления поля {data_field} без авторизации"):
            assert response.status_code == STATUS_CODE_UNAUTHORIZED, \
                f"Ожидаемый статус-код: {STATUS_CODE_UNAUTHORIZED}, полученный: {response.status_code}"

        json_response = response.json()
        with allure.step("Проверка поля 'success' в ответе"):
            assert SUCCESS in json_response, \
                f"Поле '{SUCCESS}' отсутствует в ответе"
            assert json_response[SUCCESS] is False, \
                f"Поле '{SUCCESS}' должно быть False"

        with allure.step(f"Проверка наличия сообщения об ошибке при попытке обновления поля {data_field} без авторизации"):
            assert MESSAGE in json_response, f"Поле '{MESSAGE}' отсутствует в ответе"
            assert json_response[MESSAGE] == UNAUTHORIZED_MESSAGE, \
                f"Некорректное сообщение об ошибке. Ожидалось: {UNAUTHORIZED_MESSAGE}, \
                получено: {json_response[MESSAGE]}"
