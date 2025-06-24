import random
import string
import requests
from test_data import DOMAIN, STATUS_CODE_OK, STATUS_CODE_BAD_REQUEST, INVALID_INGREDIENT_HASH, \
    STATUS_CODE_INTERNAL_SERVER_ERROR
from urls import BASE_URL

#Генераторы данных
def generate_email():
    username = generate_text(string.ascii_lowercase + string.digits)
    return f"{username}{DOMAIN}"

def generate_password():
    return generate_text(string.ascii_letters + string.digits)

def generate_name():
    return generate_text(string.ascii_letters)

def generate_text(parameter, quantity=8):
    return ''.join(random.choices(parameter, k=quantity))

def generate_valid_hash_ingredients():
    response = requests.get(f"{BASE_URL}/ingredients")
    ingredients_data = response.json().get("data", [])
    return [item["_id"] for item in ingredients_data[:2]]

INGREDIENTS_DATA = [
    (generate_valid_hash_ingredients(), STATUS_CODE_OK),
    ([], STATUS_CODE_BAD_REQUEST),
    ([INVALID_INGREDIENT_HASH], STATUS_CODE_INTERNAL_SERVER_ERROR)
]