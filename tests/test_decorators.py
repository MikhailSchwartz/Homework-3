import pytest
from src.decorators import log


def test_log_to_file_success():
    """Тест успешного выполнения с записью в файл"""
    test_filename = "log.txt"

    @log(filename=test_filename)
    def add(a, b):
        return a + b

    add(2,5)

    with open(test_filename, 'r') as file:
        content = file.read()
        assert "add ok" in content


def test_log_to_console_success(capsys):
    """Тест успешного выполнения с выводом в консоль"""

    @log()
    def multiply(a, b):
        return a * b

    multiply(4, 5)

    # Проверяем вывод в консоль
    captured = capsys.readouterr()
    assert "multiply ok" in captured.out


def test_log_to_file_error():
    """Тест ошибки с записью в файл"""
    test_filename = "log.txt"

    @log(filename=test_filename)
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    with open(test_filename, 'r') as file:
        content = file.read()
        assert "divide error" in content
        assert "ZeroDivisionError" in content
        assert "Inputs: (10, 0)" in content


def test_log_to_console_error(capsys):
    """Тест ошибки с выводом в консоль"""

    @log()
    def string_divide(a, b):
        return a / b

    with pytest.raises(TypeError):
        string_divide("10", 2)

    captured = capsys.readouterr()
    assert "string_divide error" in captured.out
    assert "TypeError" in captured.out
    assert "Inputs: ('10', 2)" in captured.out

