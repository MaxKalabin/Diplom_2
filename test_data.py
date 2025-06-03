# Базовый URL
BASE_URL = "https://stellarburgers.nomoreparties.site/api"

# Ручки из https://code.s3.yandex.net/qa-automation-engineer/python-full/diploma/api-documentation.pdf?etag=3403196b527ca03259bfd0cb41163a89
CREATE_USER_ENDPOINT = "/auth/register"
LOGIN_USER_ENDPOINT = "/auth/login"
USER_ENDPOINT = "/auth/user"
ORDER_ENDPOINT = "/orders"
INGREDIENTS_ENDPOINT = "/ingredients"


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

#Данные для параметризации
USER_DATA = ["email", "password", "name"]
LOGIN_DATA = ["email", "password"]
EDIT_DATA = ["email", "name"]

#Данные для json
NEW_DATA = 'new_data'
USER = 'user'
MESSAGE = 'message'
ORDER = 'orders'
SUCCESS = 'success'
DOMAIN = "@example.com"
DATA = "data"
ID = "_id"
AUTHORIZATION = "Authorization"
INGREDIENTS = "ingredients"
ACCESS_TOKEN = "accessToken"
EMAIL = "email"
PASSWORD = "password"
NAME = "name"

