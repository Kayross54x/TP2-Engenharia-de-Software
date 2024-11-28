import pytest
from Item import Item
from ShoppingCart import ShoppingCart

@pytest.fixture
def setup_cart():
    """Fixture para criar e configurar um carrinho de compras"""
    cart = ShoppingCart()
    cart.add_item(Item("ESM", 65.0))
    cart.add_item(Item("GoF", 120.0))
    return cart

def test_add_item(setup_cart):
    cart = setup_cart
    cart.add_item(Item("Banana", 2.0))
    assert cart.get_item_count() == 3

def test_remove_item(setup_cart):
    cart = setup_cart
    item = cart.get_items()[0]
    cart.remove_item(item)
    assert cart.get_item_count() == 1

def test_get_total_price(setup_cart):
    cart = setup_cart
    assert cart.get_total_price() == 185.0

def test_clear_cart(setup_cart):
    cart = setup_cart
    cart.clear_cart()
    assert cart.get_item_count() == 0
