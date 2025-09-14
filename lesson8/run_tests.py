import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    # Проверяем наличие необходимых переменных окружения
    required_vars = ['LOGIN', 'PASSWORD', 'COMPANY_ID', 'API_KEY']
    missing_vars = [var for var in required_vars if not os.getenv(var)]

    if missing_vars:
        print(f"Warning: Missing environment variables: {missing_vars}")
        print("Some tests will be skipped")

    # Запускаем тесты из папки tests
    exit_code = pytest.main([
        "-v",
        "--tb=short",
        "tests/",  # Указываем папку с тестами
        "-x"  # Останавливаться после первой ошибки
    ])

    sys.exit(exit_code)
