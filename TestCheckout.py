import pytest
from Checkout import Checkout  # Assuming your Checkout class is in a separate file

@pytest.fixture()
def checkout_with_prices():
    checkout = Checkout()
    checkout.addItemPrice("a", 1)
    checkout.addItemPrice("b", 2)
    return checkout

def test_CanCalculateTotal(checkout_with_prices):
    checkout_with_prices.addItem("a")
    assert checkout_with_prices.calculateTotal() == 1

def test_GetCorrectTotalWithMultipleItems(checkout_with_prices):
    checkout_with_prices.addItem("a")
    checkout_with_prices.addItem("b")
    assert checkout_with_prices.calculateTotal() == 3

def test_canAddDiscountRule(checkout_with_prices):
    checkout_with_prices.addDiscount("a", 3, 2)

@pytest.mark.skip
def test_canApplyDiscountRule(checkout_with_prices):
    checkout_with_prices.addDiscount("a", 3, 2)
    checkout_with_prices.addItem("a")
    checkout_with_prices.addItem("a")
    checkout_with_prices.addItem("a")
    assert checkout_with_prices.calculateTotal() == 2


def test_ExceptionWithBadItem(checkout_with_prices):
    with pytest.raises(Exception):
        checkout_with_prices.addItem("c")
