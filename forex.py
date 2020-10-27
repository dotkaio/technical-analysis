from .fetch import Fetch as ft_


class Forex(ft_):

    def __init__(self, *args, **kwargs):
        super(Forex, self).__init__(*args, **kwargs)
        self._append_type = False

    @ft_._output_format
    @ft_._call_api_on_func
    def get_currency_exchange_rate(self, from_currency, to_currency):
        _function = 'CURRENCY_EXCHANGE_RATE'
        return _function, 'Realtime Currency Exchange Rate', None

    @ft_._output_format
    @ft_._call_api_on_func
    def get_currency_exchange_intraday(self, from_symbol, to_symbol, interval='15min', outputsize='compact'):
        _function = 'FX_INTRADAY'
        return _function, "Time Series FX ({})".format(interval), 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_currency_exchange_daily(self, from_symbol, to_symbol, outputsize='compact'):
        _function = 'FX_DAILY'
        return _function, "Time Series FX (Daily)", 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_currency_exchange_weekly(self, from_symbol, to_symbol, outputsize='compact'):
        _function = 'FX_WEEKLY'
        return _function, "Time Series FX (Weekly)", 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_currency_exchange_monthly(self, from_symbol, to_symbol, outputsize='compact'):
        _function = 'FX_MONTHLY'
        return _function, "Time Series FX (Monthly)", 'Meta Data'
