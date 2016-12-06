from currency import Currency


class UnknownCurrencyCodeError(Exception):
    pass


class Currency_Converter:


    def __init__(self, dictionary):
        self.dictionary = dictionary


    def convert(self, currency_object, requested_currency_code):
        amount = currency_object.amount
        currency_code = currency_object.currency_code

        if currency_code == requested_currency_code:
            return currency_object
        else:
            try:
                currency_original = self.dictionary[currency_code]
                currency_new = self.dictionary[requested_currency_code]
            except KeyError:
                raise UnknownCurrencyCodeError
            conversion_rate = currency_new / currency_original
            return Currency(amount * conversion_rate, requested_currency_code)
