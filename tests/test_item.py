import pytest
from src.item import Item


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 2)


def test_calculate_total_price(item1):
    assert item1.calculate_total_price() == 20000


def test_apply_discount(item1):
    item1.pay_rate = 0.7
    item1.apply_discount()
    assert item1.price == 7000


def test_name(item1):
    assert item1.name == "Смартфон"


def test_string_to_number(item1):
    assert item1.string_to_number("15") == 15


def test_instantiate_from_csv(item1):
    assert item1.instantiate_from_csv('src/items.csv') == 10


def test_repr(item1):
    assert repr(item1) == "Item('Смартфон', 10000, 2)"


def test_str(item1):
    assert str(item1) == 'Смартфон'
