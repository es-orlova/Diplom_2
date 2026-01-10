import requests
from data import Urls

class StellarBurgersClient:
    
    @staticmethod
    def create_user(body):
        """Отправляет запрос на создание пользователя"""
        return requests.post(Urls.CREATE_USER, json=body)

    @staticmethod
    def login_user(body):
        """Отправляет запрос на логин"""
        return requests.post(Urls.LOGIN_USER, json=body)

    @staticmethod
    def delete_user(token):
        """Отправляет запрос на удаление пользователя"""
        headers = {"Authorization": token}
        return requests.delete(Urls.USER_INFO, headers=headers)
        
    @staticmethod
    def create_order(body, token=None):
        """Отправляет запрос на создание заказа"""
        headers = {"Authorization": token} if token else {}
        return requests.post(Urls.CREATE_ORDER, json=body, headers=headers)

    @staticmethod
    def get_ingredients():
        """Получает список ингредиентов"""
        return requests.get(Urls.GET_INGREDIENTS)