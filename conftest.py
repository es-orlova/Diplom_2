import pytest
import requests
import random
import string
from data import Urls

@pytest.fixture
def generate_user_data():
    """Генерирует уникальные данные для регистрации"""
    def generate_string(length=10):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    email = f"{generate_string()}@yandex.ru"
    password = generate_string()
    name = generate_string()
    return {
        "email": email,
        "password": password,
        "name": name
    }

@pytest.fixture
def create_user(generate_user_data):
    """Создает пользователя и удаляет его после теста"""
    response = requests.post(Urls.CREATE_USER, data=generate_user_data)
    token = response.json().get("accessToken")
    yield response, generate_user_data
    if token:
        requests.delete(Urls.USER_INFO, headers={"Authorization": token})

@pytest.fixture
def create_registered_user(generate_user_data):
    """Только создает пользователя и возвращает токен и данные (для тестов заказа/логина)"""
    response = requests.post(Urls.CREATE_USER, data=generate_user_data)
    token = response.json().get("accessToken")
    yield response, generate_user_data, token
    if token:
        requests.delete(Urls.USER_INFO, headers={"Authorization": token})