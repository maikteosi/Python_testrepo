# Документация проекта

## Структура проекта

lesson10/
├── pages/ # Page Object модели
│ ├── CalculatorPage.py # Страница калькулятора
│ ├── CartPage.py # Страница корзины
│ ├── CheckoutPage.py # Страница оформления заказа
│ ├── FormPage.py # Страница формы
│ ├── LoginPage.py # Страница авторизации
│ └── ProductsPage.py # Страница продуктов
├── tests/ # Тестовые сценарии
│ ├── test_01_form.py # Тесты валидации формы
│ ├── test_02_calc.py # Тесты калькулятора
│ └── test_03_shop.py # Тесты интернет-магазина
├── results/ # Результаты тестов (Allure)
├── allure-report/ # сгенерированный HTML отчет
├── requirements.txt # Зависимости проекта
└── README.md # Документация

## Описание базового синтаксиса записи и форматирования

Проект использует следующие технологии и синтаксис:

1. **Python**: Основной язык программирования для написания тестов.
2. **Selenium**: Библиотека для автоматизации взаимодействия с веб-браузером.
3. **Pytest**: Фреймворк для написания и запуска тестов.
4. **Allure**: Инструмент для генерации отчетов о выполнении тестов.

### Форматирование кода

- Код форматируется в соответствии с PEP 8 (стиль написания кода на Python).
- Используются docstrings для документирования методов и функций.
- Все шаги теста размечаются с помощью `@allure.step` или `with allure.step` для улучшения читаемости отчетов.

---

## Инструкция по запуску тестов для формирования отчета Allure

1. Установите необходимые зависимости:
   ```bash
   pip install -r requirements.txt
   ```

2. Запустите тесты с генерацией отчета Allure:
   ```bash
   pytest --alluredir=./allure_results
   ```

   Эта команда запустит все тесты и сохранит результаты в директорию `./allure_results`.

---

## Инструкция по просмотру сформированного отчета Allure

3. После завершения тестов, чтобы просмотреть отчет, выполните команду:
   ```bash
   & "$env:USERPROFILE\scoop\apps\allure\current\bin\allure.bat" serve allure_results
   ```

   Эта команда запустит локальный сервер и откроет отчет в браузере.
4. ## Генерация статического отчета для выгрузки

```bash
# Генерация HTML отчета
& "$env:USERPROFILE\scoop\apps\allure\current\bin\allure.bat" generate allure_results -o allure-report --clean

# Архивация отчета для отправки
Compress-Archive -Path allure-report -DestinationPath allure-report.zip

# Просмотр отчета
& "$env:USERPROFILE\scoop\apps\allure\current\bin\allure.bat" open allure-report
