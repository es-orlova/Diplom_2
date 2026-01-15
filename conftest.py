import pytest
import random
import string
from api_client import StellarBurgersClient

@pytest.fixture
def generate_user_data():
    """Генерирует данные для пользователя"""
    def generate_string(length=10):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return {
        "email": f"{generate_string()}@yandex.ru",
        "password": generate_string(),
        "name": generate_string()
    }

@pytest.fixture
def clean_user():
    """Фикстура принимает объекты ответов (response).В конце теста она сама проверяет, был ли создан токен, и если да — удаляет юзера."""
    responses = []
    yield responses
    for response in responses:
        token = response.json().get("accessToken")
        if token:
            StellarBurgersClient.delete_user(token)

@pytest.fixture
def get_ingredients():
    """Получаем список реальных хешей ингредиентов.Фикстура теперь доступна глобально."""
    response = StellarBurgersClient.get_ingredients()
    data = response.json().get("data", [])
    return [ingredient["_id"] for ingredient in data]

@pytest.fixture
def create_registered_user(generate_user_data):
    response = StellarBurgersClient.create_user(generate_user_data)
    token = response.json().get("accessToken")
    yield response, generate_user_data, token
    if token:
        StellarBurgersClient.delete_user(token)