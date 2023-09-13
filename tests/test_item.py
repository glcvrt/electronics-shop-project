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