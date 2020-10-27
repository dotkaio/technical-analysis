from .fetch import Fetch as ft_

class Ticker(ft_):

    @ft_._output_format
    @ft_._call_api_on_func
    def get_intraday(self, symbol, interval='15min', outputsize='compact'):

        _function = "TIME_SERIES_INTRADAY"
        return _function, "Time Series ({})".format(interval), 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_daily(self, symbol, outputsize='compact'):

        _function = "TIME_SERIES_DAILY"
        return _function, 'Time Series (Daily)', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_daily_adjusted(self, symbol, outputsize='compact'):

        _function = "TIME_SERIES_DAILY_ADJUSTED"
        return _function, 'Time Series (Daily)', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_weekly(self, symbol):

        _function = "TIME_SERIES_WEEKLY"
        return _function, 'Weekly Time Series', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_weekly_adjusted(self, symbol):

        _function = "TIME_SERIES_WEEKLY_ADJUSTED"
        return _function, 'Weekly Adjusted Time Series', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_monthly(self, symbol):

        _function = "TIME_SERIES_MONTHLY"
        return _function, 'Monthly Time Series', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_monthly_adjusted(self, symbol):

        _function = "TIME_SERIES_MONTHLY_ADJUSTED"
        return _function, 'Monthly Adjusted Time Series', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_quote_endpoint(self, symbol):

        _function = "GLOBAL_QUOTE"
        return _function, 'Global Quote', None

    @ft_._output_format
    @ft_._call_api_on_func
    def get_symbol_search(self, keywords):

        _function = "SYMBOL_SEARCH"
        return _function, 'bestMatches', None
