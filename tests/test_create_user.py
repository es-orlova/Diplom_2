import pytest
import requests
import allure
from data import Urls, ErrorMessages

@allure.suite("Создание пользователя")
class TestCreateUser:

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user_success(self, generate_user_data):
        response = requests.post(Urls.CREATE_USER, data=generate_user_data)
        if response.status_code == 200:
            token = response.json().get("accessToken")
            requests.delete(Urls.USER_INFO, headers={"Authorization": token})
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Создание пользователя, который уже зарегистрирован")
    def test_create_existing_user_fail(self, create_user):
        _, user_data = create_user
        response = requests.post(Urls.CREATE_USER, data=user_data)
        assert response.status_code == 403
        assert response.json().get("message") == ErrorMessages.USER_EXISTS

    @allure.title("Создание пользователя без обязательного поля")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_missing_field_fail(self, generate_user_data, missing_field):
        user_data = generate_user_data
        user_data.pop(missing_field)
        response = requests.post(Urls.CREATE_USER, data=user_data)
        assert response.status_code == 403
        assert response.json().get("message") == ErrorMessages.MISSING_FIELDS