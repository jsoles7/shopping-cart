# shopping-cart/test/my_test.py
import pytest


from shopping_cart import to_usd, find_product

def test_to_usd():
    #Should apply correct formatting
    assert to_usd(7.25) == "$7.25"

    #Should display two decimal places
    assert to_usd(8.5) == "$8.50"

    #Should round to two places
    assert to_usd(3.444444) == "$3.44"

    #Should display comma separators
    assert to_usd(1234567890.5555555) == "$1,234,567,890.56"


def test_find_product():
    
    #create a quick list to test 
    product_list = [
        {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
        {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
        {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
        {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25}
    ]

    # if there is a match, it should find and return a product
    product = find_product("7", product_list)
    assert product["name"] == "Pure Coconut Water With Orange"

    #the code below is taken from Prof. Rossetti's test examples
    # if there is no match, it should raise an IndexError
    with pytest.raises(IndexError):
        find_product("100", product_list)