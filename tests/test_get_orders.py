import allure
from util.helpers import get_orders
from test_data import STATUS_CODE_OK, STATUS_CODE_UNAUTHORIZED, UNAUTHORIZED_MESSAGE, ORDERS, MESSAGE, SUCCESS, TOTAL, \
    TOTAL_TODAY


@allure.feature("Получение заказов")
class TestGetOrdersWithAuth:

    @allure.title("Успешное получение заказов с авторизацией. ОР: статус 200, наличие 'orders' и счетчики заказов")
    def test_get_orders_with_auth(self, create_user_fixture):
        _, _, token = create_user_fixture
        response = get_orders(token)

        with allure.step(f"Проверка статус-кода {STATUS_CODE_OK}"):
            assert response.status_code == STATUS_CODE_OK, f"Ожидался {STATUS_CODE_OK}, получено {response.status_code}"

        with allure.step("Проверка наличия поля 'orders' в ответе"):
            assert ORDERS in response.json(), f"Поле '{ORDERS}' отсутствует в ответе"

        json_response = response.json()
        with allure.step("Проверка поля 'success' в ответе"):
            assert SUCCESS in json_response, \
                f"Поле '{SUCCESS}' отсутствует в ответе"
            assert json_response[SUCCESS] is True, \
                f"Поле '{SUCCESS}' должно быть True"

        with allure.step("Проверка наличия поля 'orders' в ответе"):
            assert ORDERS in json_response, f"Поле '{ORDERS}' отсутствует в ответе"

        with allure.step("Проверка наличия поля 'total' в ответе"):
            assert TOTAL in json_response, f"Поле '{TOTAL}' отсутствует в ответе"

        with allure.step("Проверка наличия поля 'totalToday' в ответе"):
            assert TOTAL_TODAY in json_response, f"Поле '{TOTAL_TODAY}' отсутствует в ответе"

    @allure.title("Неуспешное получение заказов без авторизации. ОР: статус 401 и сообщение об ошибке")
    def test_get_orders_without_auth(self):
        response = get_orders()

        with allure.step(f"Проверка статус-кода {STATUS_CODE_UNAUTHORIZED}"):
            assert response.status_code == STATUS_CODE_UNAUTHORIZED, \
                f"Ожидался {STATUS_CODE_UNAUTHORIZED}, получено {response.status_code}"

        with allure.step(f"Проверка сообщения об ошибке '{UNAUTHORIZED_MESSAGE}'"):
            json_response = response.json()
            assert MESSAGE in json_response, f"Поле '{MESSAGE}' отсутствует в ответе"
            assert json_response[MESSAGE] == UNAUTHORIZED_MESSAGE, \
                f"Ожидалось сообщение '{UNAUTHORIZED_MESSAGE}', получено '{json_response[MESSAGE]}'"
