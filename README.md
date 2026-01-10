# Diplom_2
# 🍔 Stellar Burgers API Tests
Автоматизированные API-тесты для сервиса Stellar Burgers. Тесты написаны на Python с использованием библиотек pytest и requests. 
Для генерации отчетов используется Allure.

# 🛠 Технологический стек
Python 3.x
Pytest — фреймворк для запуска тестов.
Requests — библиотека для отправки HTTP-запросов.
Allure — инструмент для построения отчетов о тестировании.

# 📂 Структура
Plaintext
├── conftest.py          # Фикстуры: setup/teardown (создание/удаление пользователей)
├── allure_results       # Allure-отчет
├── data.py              # Константы: URL эндпоинтов и тексты ошибок
├── requirements.txt     # Зависимости проекта
├── tests
├── ├── test_create_user.py  # Тесты ручки регистрации пользователя
├── ├── test_login_user.py   # Тесты ручки авторизации
└── └── test_orders.py       # Тесты ручки создания заказа

# 🚀 Установка и запуск
1. Предварительные требования
Убедитесь, что у вас установлен Python и Allure (как системная утилита).
Установка Allure на Mac: brew install allure
Установка Allure на Windows: через Scoop или скачав архив с официального сайта.
2. Клонирование и установка зависимостей
Клонируйте репозиторий (если применимо)
git clone <your-repo-url>
Создайте и активируйте виртуальное окружение
python -m venv venv
source venv/bin/activate  # Для Mac/Linux
venv\Scripts\activate     # Для Windows
Установите библиотеки
pip3 install -r requirements.txt
3. Запуск тестов
Простой запуск всех тестов:
pytest -v
Запуск тестов с генерацией данных для Allure-отчета:
pytest --alluredir=allure_results
4. Просмотр отчета
Чтобы увидеть красивый HTML-отчет, выполните команду:
allure serve allure_results