import pytest
import requests
import allure
from data import Urls, ErrorMessages

@allure.suite("Создание заказа")
class TestCreateOrder:

    @pytest.fixture
    def get_ingredients(self):
        """Получаем список реальных хешей ингредиентов"""
        response = requests.get(Urls.GET_INGREDIENTS)
        data = response.json()["data"]
        return [ingredient["_id"] for ingredient in data]

    @allure.title("Создание заказа с авторизацией")
    def test_create_order_authorized_success(self, create_registered_user, get_ingredients):
        _, _, token = create_registered_user
        payload = {"ingredients": [get_ingredients[0], get_ingredients[1]]}
        headers = {"Authorization": token}
        response = requests.post(Urls.CREATE_ORDER, data=payload, headers=headers)
        assert response.status_code == 200
        assert response.json().get("success") is True
        assert "order" in response.json()

    @allure.title("Создание заказа без авторизации")
    def test_create_order_unauthorized_success(self, get_ingredients):
        payload = {"ingredients": [get_ingredients[0], get_ingredients[1]]}
        response = requests.post(Urls.CREATE_ORDER, data=payload)
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients_success(self, get_ingredients):
        payload = {"ingredients": get_ingredients[:2]} # Берем два первых ингредиента
        response = requests.post(Urls.CREATE_ORDER, data=payload)
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_no_ingredients_fail(self, create_registered_user):
        _, _, token = create_registered_user
        headers = {"Authorization": token}
        payload = {"ingredients": []}
        response = requests.post(Urls.CREATE_ORDER, data=payload, headers=headers)
        assert response.status_code == 400
        assert response.json().get("message") == ErrorMessages.NO_INGREDIENTS

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_invalid_hash_fail(self, create_registered_user):
        _, _, token = create_registered_user
        headers = {"Authorization": token}
        payload = {"ingredients": ["invalid_hash_123", "another_invalid_hash"]}
        response = requests.post(Urls.CREATE_ORDER, data=payload, headers=headers)
        assert response.status_code == 500