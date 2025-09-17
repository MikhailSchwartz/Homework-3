import pytest
from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_executed(banking_operations, banking_operations_executed):
    """Тест фильтрации по статусу EXECUTED"""
    assert filter_by_state(banking_operations, "EXECUTED") == banking_operations_executed


def test_filter_by_state_canceled(banking_operations, banking_operations_canceled):
    """Тест фильтрации по статусу CANCELED"""
    assert filter_by_state(banking_operations, "CANCELED") == banking_operations_canceled


def test_filter_by_state_accepted(banking_operations):
    """Тест фильтрации по не существующему статусу ACCEPTED"""
    assert filter_by_state(banking_operations, "ACCEPTED") == "Операции со статусом ACCEPTED отсутствуют"


def test_sort_by_date_true(banking_operations, sorted_true):
    """Тест сортировки списков order=True"""
    assert sort_by_date(banking_operations) == sorted_true


def test_sort_by_date_false(banking_operations, sorted_false):
    """Тест сортировки списков order=False"""
    assert sort_by_date(banking_operations, order=False) == sorted_false


def test_sort_by_date_same_date_true(banking_operations_same_date, sorted_same_date_true):
    """Тест сортировки списков с одиноковыми датами order=True"""
    assert sort_by_date(banking_operations_same_date, order=True) == sorted_same_date_true


def test_sort_by_date_same_date_false(banking_operations_same_date, sorted_same_date_false):
    """Тест сортировки списков с одиноковыми датами order=False"""
    assert sort_by_date(banking_operations_same_date, order=False) == sorted_same_date_false