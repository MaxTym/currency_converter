class DifferentCurrencyCodeError(Exception):
    pass


class Currency:


    def __init__(self, amount, currency_code=None):
        if currency_code is not None:
            self.amount = amount
            self.currency_code = currency_code
        else:
            currency_symbol_dict = {'$' : 'USD', '€' : 'EUR', '₴' : 'UAH'}
            symbol_amount_list = list(amount)
            currency_symbol = symbol_amount_list[0]
            self.currency_code = currency_symbol_dict[currency_symbol]
            self.amount = float(''.join(symbol_amount_list[1:]))


    def __eq__(self, other):
        return self.amount == other.amount and self.currency_code == other.currency_code


    def __add__(self, other):
        if self.currency_code != other.currency_code:
            raise DifferentCurrencyCodeError
        else:
            return Currency(self.amount + other.amount, self.currency_code)


    def __sub__(self, other):
        if self.currency_code != other.currency_code:
            raise DifferentCurrencyCodeError
        else:
            return Currency(self.amount - other.amount, self.currency_code)


    def __mul__(self, other):
        return Currency(self.amount * other, self.currency_code)
