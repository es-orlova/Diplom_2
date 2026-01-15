import pytest
import allure
from api_client import StellarBurgersClient
from data import ErrorMessages

@allure.suite("Создание пользователя")
class TestCreateUser:

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user_success(self, generate_user_data, clean_user):
        response = StellarBurgersClient.create_user(generate_user_data)
        clean_user.append(response)
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Создание пользователя, который уже зарегистрирован")
    def test_create_existing_user_fail(self, create_registered_user):
        user_data = create_registered_user[1]
        response = StellarBurgersClient.create_user(user_data)
        assert response.status_code == 403
        assert response.json().get("message") == ErrorMessages.USER_EXISTS

    @allure.title("Создание пользователя без обязательного поля")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_missing_field_fail(self, generate_user_data, missing_field):
        user_data = generate_user_data
        user_data.pop(missing_field)
        response = StellarBurgersClient.create_user(user_data)
        assert response.status_code == 403
        assert response.json().get("message") == ErrorMessages.MISSING_FIELDS