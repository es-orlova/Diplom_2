import requests
import allure
from data import Urls

class StellarBurgersClient:
    
    @staticmethod
    @allure.step("Создание пользователя")
    def create_user(body):
        """Отправляет запрос на создание пользователя"""
        return requests.post(Urls.CREATE_USER, json=body)

    @staticmethod
    @allure.step("Логин пользователя")
    def login_user(body):
        """Отправляет запрос на логин"""
        return requests.post(Urls.LOGIN_USER, json=body)

    @staticmethod
    @allure.step("Удаление пользователя")
    def delete_user(token):
        """Отправляет запрос на удаление пользователя"""
        headers = {"Authorization": token}
        return requests.delete(Urls.USER_INFO, headers=headers)
        
    @staticmethod
    @allure.step("Создание заказа")
    def create_order(body, token=None):
        """Отправляет запрос на создание заказа"""
        headers = {"Authorization": token} if token else {}
        return requests.post(Urls.CREATE_ORDER, json=body, headers=headers)

    @staticmethod
    @allure.step("Получение списка ингредиентов")
    def get_ingredients():
        """Получает список ингредиентов"""
        return requests.get(Urls.GET_INGREDIENTS)