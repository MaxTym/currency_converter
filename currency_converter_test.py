from nose.tools import raises
from currency import Currency
from currency_converter import UnknownCurrencyCodeError
from currency_converter import Currency_Converter


currency_dictionary = {'USD': 1.0, 'EUR': 0.74, 'UAH' : 25.0}
converter = Currency_Converter(currency_dictionary)


def test_create_currency_converter():
    assert converter.dictionary == currency_dictionary


def test_convert_to_same_currency_code():
    assert converter.convert(Currency(1, 'USD'), 'USD') == Currency(1, 'USD')


def test_convert_to_different_currency_code():
    curr1 = Currency(1.0, 'USD')
    curr2 = Currency(0.74, 'EUR')
    curr3 = Currency(25.0, 'UAH')
    assert converter.convert(curr1, 'EUR') == curr2
    assert converter.convert(curr1, 'UAH') == curr3
    assert converter.convert(curr2, 'UAH') == curr3
    assert converter.convert(curr3, 'EUR') == curr2


@raises(UnknownCurrencyCodeError)
def test_convert_from_unknown_currency_code():
    converter.convert(Currency(1.0, 'CAN'), 'USD')


@raises(UnknownCurrencyCodeError)
def test_convert_to_unknown_currency_code():
    converter.convert(Currency(1.0, 'USD'), 'CAN')
