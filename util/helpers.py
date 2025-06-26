import requests
import json
from test_data import AUTHORIZATION, INGREDIENTS
from urls import BASE_URL, CREATE_USER_ENDPOINT, LOGIN_USER_ENDPOINT, USER_ENDPOINT, ORDER_ENDPOINT, \
    INGREDIENTS_ENDPOINT

#Запросы, использую что бы не делать сложные конструкции в запросах
def get(path, headers=None):
    return requests.get(f"{BASE_URL}{path}", headers=headers)

def post(path, payload=None, headers=None):
    return requests.post(f"{BASE_URL}{path}", json=payload, headers=headers)

def patch(path, payload=None, headers=None):
    return requests.patch(f"{BASE_URL}{path}", json=payload, headers=headers)

def delete(path, payload=None, headers=None):
    return requests.delete(f"{BASE_URL}{path}", json=payload, headers=headers)

#Ручки для работы с пользователями
def create_user(payload):
    return post(CREATE_USER_ENDPOINT, payload)

def login_user(payload):
    return post(LOGIN_USER_ENDPOINT, payload)

def edit_user(payload, token=None):
    headers = {AUTHORIZATION: token} if token else None
    return patch(USER_ENDPOINT, payload, headers=headers)

def delete_user(token):
    headers = {AUTHORIZATION: token}
    return delete(USER_ENDPOINT, headers=headers)

#Ручки для работы с заказами
def create_order(ingredients, token=None):
    headers = {AUTHORIZATION: token} if token else None
    return post(ORDER_ENDPOINT, {INGREDIENTS: ingredients}, headers=headers)

def get_orders(token=None):
    headers = {AUTHORIZATION: token} if token else None
    return get(ORDER_ENDPOINT, headers=headers)

def get_ingredients():
    return get(INGREDIENTS_ENDPOINT)

#Обработка ответа для безопасного извлечения JSON из ответа (при 500 ошибках)
def parse_json(response):
    try:
        return response.json()
    except json.JSONDecodeError:
        return {}


