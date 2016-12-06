from nose.tools import raises
from currency import Currency
from currency import DifferentCurrencyCodeError


def test_create_currency_with_amount_and_code():
    one_dollar = Currency(1, 'USD')
    assert one_dollar.amount == 1
    assert one_dollar.currency_code == 'USD'


def test_currency_with_same_amount_and_code_are_equal():
    curr1 = Currency(99, 'USD')
    curr2 = Currency(99, 'USD')
    assert curr1 == curr2


def test_currency_with_different_amounts_are_not_equal():
    curr1 = Currency(1, 'USD')
    curr2 = Currency(99, 'USD')
    assert curr1 != curr2


def test_currency_with_different_codes_are_not_equal():
    curr1 = Currency(1, 'USD')
    curr2 = Currency(1, 'EUR')
    assert curr1 != curr2


def test_addition_to_currency_with_same_code():
    curr1 = Currency(1, 'USD')
    curr2 = Currency(10, 'USD')
    assert curr1 + curr2 == Currency(11, 'USD')


def test_subtraction_from_currency_with_same_code():
    curr1 = Currency(10, 'USD')
    curr2 = Currency(1, 'USD')
    assert curr1 - curr2 == Currency(9, 'USD')


@raises(DifferentCurrencyCodeError)
def test_raise_different_currency_code_error():
    curr1 = Currency(1, 'USD')
    curr2 = Currency(1, 'EUR')
    curr1 + curr2
    curr1 - curr2


def test_multiplication_by_int_float():
    assert Currency(10, 'USD') * 5 == Currency(50, 'USD')
    assert Currency(10, 'USD') * 2.0 == Currency(20.0, 'USD')


def test_create_currency_with_one_parameter():
    assert Currency('$1') == Currency(1, 'USD')
    assert Currency('€7.00') == Currency(7.00, 'EUR')
