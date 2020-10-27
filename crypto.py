from .fetch import Fetch as ft_

class Crypto(ft_):
    @ft_._output_format
    @ft_._call_api_on_func
    def get_digital_currency_daily(self, symbol, market):
        _FUNCTION_KEY = 'DIGITAL_CURRENCY_DAILY'
        return _FUNCTION_KEY, 'Time Series (Digital Currency Daily)', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_digital_currency_weekly(self, symbol, market):
        _FUNCTION_KEY = 'DIGITAL_CURRENCY_WEEKLY'
        return _FUNCTION_KEY, 'Time Series (Digital Currency Weekly)', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_digital_currency_monthly(self, symbol, market):
        _FUNCTION_KEY = 'DIGITAL_CURRENCY_MONTHLY'
        return _FUNCTION_KEY, 'Time Series (Digital Currency Monthly)', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_digital_currency_exchange_rate(self, symbol, market):
        _FUNCTION_KEY = 'CURRENCY_EXCHANGE_RATE'
        return _FUNCTION_KEY, 'Dictonary (Digital Currency Exchange Rate)', 'Meta Data'
