import pytest
from string_utils import StringUtils


string_utils = StringUtils()

# Тесты для capitalize()
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("123", "123"),    # числа как строка
    ("04 апреля 2023", "04 апреля 2023")  # строка с пробелами и числами
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    (None, None),  # проверка на None
    ([], [])       # пустой список
])
def test_capitalize_negative(input_str, expected):
    if input_str is None or isinstance(input_str, list):
        with pytest.raises((TypeError, AttributeError)):
            string_utils.capitalize(input_str)
    else:
        assert string_utils.capitalize(input_str) == expected

# Тесты для trim()
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("  skypro", "skypro"),
    ("   hello world", "hello world"),
    (" \tpython", "\tpython"),
    ("  123", "123"),    # числа
    ("  04 апреля 2023", "04 апреля 2023")  # дата
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "skypro"),
    ("", ""),
    ("    ", ""),
    (None, None),
    ([], [])
])
def test_trim_negative(input_str, expected):
    if input_str is None or isinstance(input_str, list):
        with pytest.raises((TypeError, AttributeError)):
            string_utils.trim(input_str)
    else:
        assert string_utils.trim(input_str) == expected

# Тесты для contains()
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("hello world", " ", True),
    ("python", "p", True),
    ("123", "2", True),   # число как символ
    ("04 апреля 2023", " ", True)  # пробел
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "s", False),
    ("hello", "x", False),
    ("", "a", False),
    (None, "a", False),
])
def test_contains_negative(string, symbol, expected):
    if string is None or isinstance(string, list):
        with pytest.raises((TypeError, AttributeError)):
            string_utils.contains(string, symbol)
    else:
        assert string_utils.contains(string, symbol) == expected

# Тесты для delete_symbol()
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("banana", "a", "bnn"),
    ("hello world", " ", "helloworld"),
    ("12345", "2", "1345"),  # числа
    ("04 апреля 2023", " ", "04апреля2023")  # пробелы
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "X", "SkyPro"),
    ("", "a", ""),
    ("hello", "", "hello"),
    (None, "a", None),
])
def test_delete_symbol_negative(string, symbol, expected):
    if string is None or isinstance(string, list):
        with pytest.raises((TypeError, AttributeError)):
            string_utils.delete_symbol(string, symbol)
    else:
        assert string_utils.delete_symbol(string, symbol) == expected