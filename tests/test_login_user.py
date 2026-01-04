import requests
import allure
from data import Urls, ErrorMessages

@allure.suite("Логин пользователя")
class TestLoginUser:

    @allure.title("Вход под существующим пользователем")
    def test_login_existing_user_success(self, create_registered_user):
        _, user_data, _ = create_registered_user
        
        payload = {
            "email": user_data["email"],
            "password": user_data["password"]
        }
        response = requests.post(Urls.LOGIN_USER, data=payload)
        assert response.status_code == 200
        assert response.json().get("success") is True
        assert "accessToken" in response.json()

    @allure.title("Вход с неверным логином или паролем")
    def test_login_wrong_credentials_fail(self, generate_user_data):
        payload = {
            "email": generate_user_data["email"],
            "password": "wrong_password"
        }
        response = requests.post(Urls.LOGIN_USER, data=payload)
        assert response.status_code == 401
        assert response.json().get("success") is False