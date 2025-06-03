import allure
from helpers import get_orders
from test_data import STATUS_CODE_OK, STATUS_CODE_UNAUTHORIZED, UNAUTHORIZED_MESSAGE, ORDER, MESSAGE

@allure.feature("Получение заказов")
class TestGetOrdersWithAuth:

    @allure.title("Успешное получение заказов с авторизацией - возвращается ожидаемый статус 200")
    def test_get_orders_with_auth_status_200(self, create_user_fixture):
        _, _, token = create_user_fixture
        response = get_orders(token)
        assert response.status_code == STATUS_CODE_OK

    @allure.title("Успешное получение заказов с авторизацией - в ответе есть 'orders'")
    def test_get_orders_with_auth_has_orders(self, create_user_fixture):
        _, _, token = create_user_fixture
        response = get_orders(token)
        assert ORDER in response.json()

    @allure.title("Неуспешное получение заказов без авторизации - возвращается ожидаемый статус 401")
    def test_get_orders_without_auth_status_401 (self):
        response = get_orders()
        assert response.status_code == STATUS_CODE_UNAUTHORIZED

    @allure.title("Неуспешное получение заказов без авторизации - возвращается ожидаемое сообщение")
    def test_get_orders_without_auth_unauthorized_message(self):
        response = get_orders()
        assert response.json()[MESSAGE] == UNAUTHORIZED_MESSAGE