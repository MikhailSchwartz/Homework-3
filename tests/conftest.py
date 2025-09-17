import pytest


@pytest.fixture()
def invalid_data_iso():
    """Фикстура даты без 'T'"""
    return "2024-03-1102:26:18.671407"


@pytest.fixture()
def banking_operations():
    """Фикстура со списком словарей с информацией о банковских операциях"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture()
def banking_operations_executed():
    """Фикстура со списком словарей которая возращает функция filter_by_state при значении ключа stste: EXECUTED"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture()
def banking_operations_canceled():
    """Фикстура со списком словарей которая возращает функция filter_by_state при значении ключа stste: CANCELED"""
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture()
def sorted_false():
    """Фикстура со списком словарей которая возращает функция sort_by_date при аргументе order=False"""
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture()
def sorted_true():
    """Фикстура со списком словарей которая возращает функция sort_by_date при аргументе order=True"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture()
def banking_operations_same_date():
    """Фикстура со списком словарей с информацией о банковских операциях, с одинаковыми датами"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-06-30T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-06-30T08:21:33.419441"},
    ]


@pytest.fixture()
def sorted_same_date_false():
    """Фикстура со списком словарей с одинаковыми датами,
     которая возращает функция sort_by_date при аргументе order=False"""
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-06-30T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-06-30T21:27:25.241689"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture()
def sorted_same_date_true():
    """Фикстура со списком словарей с одинаковыми датами,
         которая возращает функция sort_by_date при аргументе order=True"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-06-30T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-06-30T08:21:33.419441"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
