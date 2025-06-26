# Текст всех ошибок
USER_ALREADY_EXISTS = "User already exists"
REQUIRED_FIELDS_MESSAGE = "Email, password and name are required fields"
UNAUTHORIZED_MESSAGE = "You should be authorised"
INVALID_CREDENTIALS_MESSAGE = "email or password are incorrect"

# Коды всех ошибок
STATUS_CODE_OK = 200
STATUS_CODE_BAD_REQUEST = 400
STATUS_CODE_UNAUTHORIZED = 401
STATUS_CODE_FORBIDDEN = 403
STATUS_CODE_INTERNAL_SERVER_ERROR = 500

# Хеши ингредиентов
INVALID_INGREDIENT_HASH = "invalidhash123"
INGREDIENTS_ERRORS = [
    ([], STATUS_CODE_BAD_REQUEST, "Ingredient ids must be provided", False),
    ([INVALID_INGREDIENT_HASH], STATUS_CODE_INTERNAL_SERVER_ERROR, None, None)
]

#Данные для параметризации
USER_DATA = ["email", "password", "name"]
LOGIN_DATA = ["email", "password"]
EDIT_DATA = ["email", "name"]

#Данные для json
NEW_DATA = 'new_data'
USER = 'user'
MESSAGE = 'message'
ORDERS = 'orders'
SUCCESS = 'success'
DOMAIN = "@example.com"
AUTHORIZATION = "Authorization"
INGREDIENTS = "ingredients"
ACCESS_TOKEN = "accessToken"
REFRESH_TOKEN = "refreshToken"
EMAIL = "email"
PASSWORD = "password"
NAME = "name"
ORDER = "order"
NUMBER = "number"
TOTAL = "total"
TOTAL_TODAY = "totalToday"