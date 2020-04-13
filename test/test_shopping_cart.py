# shopping-cart/test/my_test.py

from shopping_cart import to_usd

def test_to_usd():
    #Should apply correct formatting
    assert to_usd(7.25) == "$7.25"

    #Should display two decimal places
    assert to_usd(8.5) == "$8.50"

    #Should round to two places
    assert to_usd(3.444444) == "$3.44"

    #Should display comma separators
    assert to_usd(1234567890.5555555) == "$1,234,567,890.56"