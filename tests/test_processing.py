import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_executed(banking_operations: list, banking_operations_executed: list) -> None:
    """Тест фильтрации по статусу EXECUTED"""
    assert filter_by_state(banking_operations, "EXECUTED") == banking_operations_executed


def test_filter_by_state_canceled(banking_operations: list, banking_operations_canceled: list) -> None:
    """Тест фильтрации по статусу CANCELED"""
    assert filter_by_state(banking_operations, "CANCELED") == banking_operations_canceled


def test_filter_by_state_accepted(banking_operations: list) -> None:
    """Тест фильтрации по не существующему статусу ACCEPTED"""
    with pytest.raises(ValueError) as exc_info:
        filter_by_state(banking_operations, "ACCEPTED")

    assert str(exc_info.value) == "Операции со статусом ACCEPTED отсутствуют"


def test_sort_by_date_true(banking_operations: list, sorted_true: list) -> None:
    """Тест сортировки списков order=True"""
    assert sort_by_date(banking_operations) == sorted_true


def test_sort_by_date_false(banking_operations: list, sorted_false: list) -> None:
    """Тест сортировки списков order=False"""
    assert sort_by_date(banking_operations, order=False) == sorted_false


def test_sort_by_date_same_date_true(banking_operations_same_date: list, sorted_same_date_true: list) -> None:
    """Тест сортировки списков с одиноковыми датами order=True"""
    assert sort_by_date(banking_operations_same_date, order=True) == sorted_same_date_true


def test_sort_by_date_same_date_false(banking_operations_same_date: list, sorted_same_date_false: list) -> None:
    """Тест сортировки списков с одиноковыми датами order=False"""
    assert sort_by_date(banking_operations_same_date, order=False) == sorted_same_date_false
