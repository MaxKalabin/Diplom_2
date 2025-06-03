import allure
import pytest
from helpers import create_user, delete_user, generate_email, generate_password, generate_name
from test_data import ACCESS_TOKEN, EMAIL, PASSWORD, NAME

@allure.step("Создание пользователя")
@pytest.fixture()
def create_user_fixture(generate_user_data):
    response = create_user(generate_user_data)
    access_token = response.json()[ACCESS_TOKEN]
    yield generate_user_data, response, access_token
    with allure.step("Удаление пользователя после теста"):
        delete_user(access_token)

@allure.step("Генерация данных пользователя")
@pytest.fixture()
def generate_user_data():
    return ({
        EMAIL : generate_email(),
        PASSWORD : generate_password(),
        NAME : generate_name()
    })