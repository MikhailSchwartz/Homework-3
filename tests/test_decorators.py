import pytest

from src.decorators import log


def test_log_to_file() -> None:
    """Тест успешного выполнения с записью в файл"""
    test_filename = "log.txt"

    open(test_filename, "w").close()

    @log(filename=test_filename)
    def add(a: int, b: int) -> int:
        return a + b

    add(2, 5)

    with open(test_filename, "r") as file:
        content = file.read()
        assert "add ok" in content


def test_log_to_console(capsys) -> None:
    """Тест успешного выполнения с выводом в консоль"""

    @log()
    def multiply(a: int, b: int) -> int:
        return a * b

    multiply(4, 5)

    # Проверяем вывод в консоль
    captured = capsys.readouterr()
    assert "multiply ok" in captured.out


def test_log_to_file_error() -> None:
    """Тест ошибки с записью в файл"""
    test_filename = "log.txt"

    open(test_filename, "w").close()

    @log(filename=test_filename)
    def divide(a: int, b: int) -> float:
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    with open(test_filename, "r") as file:
        content = file.read()
        assert content == "divide error: ZeroDivisionError. Inputs: (10, 0), {}\n"


def test_log_to_console_error(capsys) -> None:
    """Тест ошибки с выводом в консоль"""

    @log()
    def subtraction(a: int, b: int) -> float:
        return a / b

    with pytest.raises(TypeError):
        subtraction("ы", 2)

    captured = capsys.readouterr()
    assert captured.out == "subtraction error: TypeError. Inputs: ('ы', 2), {}\n"
