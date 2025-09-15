# Yougile API Autotests

## Установка
1. Клонировать репозиторий
2. Установить зависимости: `pip install -r requirements.txt`
3. Скопировать `.env.example` в `.env` и заполнить данными
4. Запустить тесты: `python run_tests.py`

## Структура проекта
lesson8/
├── tests/
│   ├── test_auth_api.py
│   ├── test_project_api.py
│   └── __init__.py
├── src/
│   ├── config.py
│   ├── yougile_api.py
│   └── __init__.py
├── .env
├── .env.example
├── requirements.txt
├── pytest.ini
└── run_tests.py
└── README lesson8.md