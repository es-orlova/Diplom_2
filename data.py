class Urls:
    BASE_URL = 'https://stellarburgers.education-services.ru/api'
    
    CREATE_USER = f'{BASE_URL}/auth/register'
    LOGIN_USER = f'{BASE_URL}/auth/login'
    USER_INFO = f'{BASE_URL}/auth/user'
    GET_INGREDIENTS = f'{BASE_URL}/ingredients'
    CREATE_ORDER = f'{BASE_URL}/orders'

class ErrorMessages:
    USER_EXISTS = "User already exists"
    MISSING_FIELDS = "Email, password and name are required fields"
    LOGIN_FAILED = "email or password are incorrect"
    NO_INGREDIENTS = "Ingredient ids must be provided"