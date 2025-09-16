import pytest
from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_executed(banking_operations):
    """Тест фильтрации по статусу EXECUTED"""
    result = filter_by_state(banking_operations, "EXECUTED")
    assert filter_by_state(banking_operations, "EXECUTED") == result
    assert len(result) == 2


def test_filter_by_state_canceled(banking_operations):
    """Тест фильтрации по статусу CANCELED"""
    result = filter_by_state(banking_operations, "CANCELED")
    assert filter_by_state(banking_operations, "CANCELED") == result
    assert len(result) == 2


def test_filter_by_state_accepted(banking_operations):
    """Тест фильтрации по статусу ACCEPTED"""
    assert filter_by_state(banking_operations, "ACCEPTED") == "Операции со статусом ACCEPTED отсутствуют"


