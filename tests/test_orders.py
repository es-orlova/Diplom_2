import allure
from api_client import StellarBurgersClient
from data import ErrorMessages

@allure.suite("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа с авторизацией")
    def test_create_order_authorized_success(self, create_registered_user, get_ingredients):
        _, _, token = create_registered_user
        payload = {"ingredients": [get_ingredients[0], get_ingredients[1]]}
        response = StellarBurgersClient.create_order(payload, token=token)
        assert response.status_code == 200
        assert response.json().get("success") is True
        assert "order" in response.json()

    @allure.title("Создание заказа без авторизации")
    def test_create_order_unauthorized_success(self, get_ingredients):
        payload = {"ingredients": [get_ingredients[0], get_ingredients[1]]}
        response = StellarBurgersClient.create_order(payload)
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients_success(self, get_ingredients):
        payload = {"ingredients": get_ingredients[:2]} 
        response = StellarBurgersClient.create_order(payload)
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_no_ingredients_fail(self, create_registered_user):
        _, _, token = create_registered_user
        payload = {"ingredients": []}
        response = StellarBurgersClient.create_order(payload, token=token)
        assert response.status_code == 400
        assert response.json().get("message") == ErrorMessages.NO_INGREDIENTS

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_invalid_hash_fail(self, create_registered_user):
        _, _, token = create_registered_user
        payload = {"ingredients": ["invalid_hash_123", "another_invalid_hash"]}
        response = StellarBurgersClient.create_order(payload, token=token)
        assert response.status_code == 500