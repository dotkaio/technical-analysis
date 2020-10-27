from .fetch import Fetch as ft_

class Indicator(ft_):

    def __init__(self, *args, **kwargs):
        """ Inherit Fetch """

        super(Indicator, self).__init__(*args, **kwargs)
        self._append_type = False

    @ft_._output_format
    @ft_._call_api_on_func
    def get_sma(self, symbol, interval='daily', time_period=20, series_type='close'):
        _function = "SMA"
        return _function, 'Technical Analysis: SMA', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_ema(self, symbol, interval='daily', time_period=20, series_type='close'):
        _function = "EMA"
        return _function, 'Technical Analysis: EMA', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_wma(self, symbol, interval='daily', time_period=20, series_type='close'):
        _function = "WMA"
        return _function, 'Technical Analysis: WMA', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_dema(self, symbol, interval='daily', time_period=20, series_type='close'):

        _function = "DEMA"
        return _function, 'Technical Analysis: DEMA', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_tema(self, symbol, interval='daily', time_period=20, series_type='close'):

        _function = "TEMA"
        return _function, 'Technical Analysis: TEMA', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_trima(self, symbol, interval='daily', time_period=20, series_type='close'):
        _function = "TRIMA"
        return _function, 'Technical Analysis: TRIMA', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_kama(self, symbol, interval='daily', time_period=20, series_type='close'):
        _function = "KAMA"
        return _function, 'Technical Analysis: KAMA', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_mama(self, symbol, interval='daily', series_type='close',
                 fastlimit=None, slowlimit=None):
        _function = "MAMA"
        return _function, 'Technical Analysis: MAMA', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_vwap(self, symbol, interval='5min'):
        _function = "VWAP"
        return _function, 'Technical Analysis: VWAP', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_t3(self, symbol, interval='daily', time_period=20, series_type='close'):
        _function = "T3"
        return _function, 'Technical Analysis: T3', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_macd(self, symbol, interval='daily', series_type='close',
                 fastperiod=None, slowperiod=None, signalperiod=None):
        _function = "MACD"
        return _function, 'Technical Analysis: MACD', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_macdext(self, symbol, interval='daily', series_type='close',
                    fastperiod=None, slowperiod=None, signalperiod=None, fastmatype=None,
                    slowmatype=None, signalmatype=None):
        _function = "MACDEXT"
        return _function, 'Technical Analysis: MACDEXT', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_stoch(self, symbol, interval='daily', fastkperiod=None,
                  slowkperiod=None, slowdperiod=None, slowkmatype=None, slowdmatype=None):
        _function = "STOCH"
        return _function, 'Technical Analysis: STOCH', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_stochf(self, symbol, interval='daily', fastkperiod=None,
                   fastdperiod=None, fastdmatype=None):
        _function = "STOCHF"
        return _function, 'Technical Analysis: STOCHF', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_rsi(self, symbol, interval='daily', time_period=20, series_type='close'):
        _function = "RSI"
        return _function, 'Technical Analysis: RSI', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_stochrsi(self, symbol, interval='daily', time_period=20,
                     series_type='close', fastkperiod=None, fastdperiod=None, fastdmatype=None):
        _function = "STOCHRSI"
        return _function, 'Technical Analysis: STOCHRSI', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_willr(self, symbol, interval='daily', time_period=20):
        _function = "WILLR"
        return _function, 'Technical Analysis: WILLR', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_adx(self, symbol, interval='daily', time_period=20):
        _function = "ADX"
        return _function, 'Technical Analysis: ADX', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_adxr(self, symbol, interval='daily', time_period=20):
        _function = "ADXR"
        return _function, 'Technical Analysis: ADXR', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_apo(self, symbol, interval='daily', series_type='close',
                fastperiod=None, slowperiod=None, matype=None):
        _function = "APO"
        return _function, 'Technical Analysis: APO', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_ppo(self, symbol, interval='daily', series_type='close',
                fastperiod=None, slowperiod=None, matype=None):
        _function = "PPO"
        return _function, 'Technical Analysis: PPO', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_mom(self, symbol, interval='daily', time_period=20, series_type='close'):
        _function = "MOM"
        return _function, 'Technical Analysis: MOM', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_bop(self, symbol, interval='daily', time_period=20):
        _function = "BOP"
        return _function, 'Technical Analysis: BOP', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_cci(self, symbol, interval='daily', time_period=20):
        _function = "CCI"
        return _function, 'Technical Analysis: CCI', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_cmo(self, symbol, interval='daily', time_period=20, series_type='close'):
        _function = "CMO"
        return _function, 'Technical Analysis: CMO', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_roc(self, symbol, interval='daily', time_period=20, series_type='close'):
        _function = "ROC"
        return _function, 'Technical Analysis: ROC', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_rocr(self, symbol, interval='daily', time_period=20, series_type='close'):
        _function = "ROCR"
        return _function, 'Technical Analysis: ROCR', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_aroon(self, symbol, interval='daily', time_period=20, series_type='close'):
        _function = "AROON"
        return _function, 'Technical Analysis: AROON', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_aroonosc(self, symbol, interval='daily', time_period=20, series_type='close'):
        _function = "AROONOSC"
        return _function, 'Technical Analysis: AROONOSC', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_mfi(self, symbol, interval='daily', time_period=20, series_type='close'):
        _function = "MFI"
        return _function, 'Technical Analysis: MFI', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_trix(self, symbol, interval='daily', time_period=20, series_type='close'):
        _function = "TRIX"
        return _function, 'Technical Analysis: TRIX', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_ultosc(self, symbol, interval='daily', timeperiod1=None,
                   timeperiod2=None, timeperiod3=None):
        _function = "ULTOSC"
        return _function, 'Technical Analysis: ULTOSC', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_dx(self, symbol, interval='daily', time_period=20, series_type='close'):
        _function = "DX"
        return _function, 'Technical Analysis: DX', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_minus_di(self, symbol, interval='daily', time_period=20):
        _function = "MINUS_DI"
        return _function, 'Technical Analysis: MINUS_DI', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_plus_di(self, symbol, interval='daily', time_period=20):
        _function = "PLUS_DI"
        return _function, 'Technical Analysis: PLUS_DI', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_minus_dm(self, symbol, interval='daily', time_period=20):
        _function = "MINUS_DM"
        return _function, 'Technical Analysis: MINUS_DM', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_plus_dm(self, symbol, interval='daily', time_period=20):
        _function = "PLUS_DM"
        return _function, 'Technical Analysis: PLUS_DM', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_bbands(self, symbol, interval='daily', time_period=20,  series_type='close',
                   nbdevup=None, nbdevdn=None, matype=None):
        _function = "BBANDS"
        return _function, 'Technical Analysis: BBANDS', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_midpoint(self, symbol, interval='daily', time_period=20, series_type='close'):
        _function = "MIDPOINT"
        return _function, 'Technical Analysis: MIDPOINT', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_midprice(self, symbol, interval='daily', time_period=20):
        _function = "MIDPRICE"
        return _function, 'Technical Analysis: MIDPRICE', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_sar(self, symbol, interval='daily', acceleration=None, maximum=None):
        _function = "SAR"
        return _function, 'Technical Analysis: SAR', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_trange(self, symbol, interval='daily'):
        _function = "TRANGE"
        return _function, 'Technical Analysis: TRANGE', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_atr(self, symbol, interval='daily', time_period=20):
        _function = "ATR"
        return _function, 'Technical Analysis: ATR', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_natr(self, symbol, interval='daily', time_period=20):
        _function = "NATR"
        return _function, 'Technical Analysis: NATR', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_ad(self, symbol, interval='daily'):
        _function = "AD"
        return _function, 'Technical Analysis: Chaikin A/D', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_adosc(self, symbol, interval='daily', fastperiod=None,
                  slowperiod=None):
        _function = "ADOSC"
        return _function, 'Technical Analysis: ADOSC', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_obv(self, symbol, interval='daily'):
        _function = "OBV"
        return _function, 'Technical Analysis: OBV', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_ht_trendline(self, symbol, interval='daily', series_type='close'):
        _function = "HT_TRENDLINE"
        return _function, 'Technical Analysis: HT_TRENDLINE', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_ht_sine(self, symbol, interval='daily', series_type='close'):
        _function = "HT_SINE"
        return _function, 'Technical Analysis: HT_SINE', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_ht_trendmode(self, symbol, interval='daily', series_type='close'):
        _function = "HT_TRENDMODE"
        return _function, 'Technical Analysis: HT_TRENDMODE', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_ht_dcperiod(self, symbol, interval='daily', series_type='close'):
        _function = "HT_DCPERIOD"
        return _function, 'Technical Analysis: HT_DCPERIOD', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_ht_dcphase(self, symbol, interval='daily', series_type='close'):
        _function = "HT_DCPHASE"
        return _function, 'Technical Analysis: HT_DCPHASE', 'Meta Data'

    @ft_._output_format
    @ft_._call_api_on_func
    def get_ht_phasor(self, symbol, interval='daily', series_type='close'):
        _function = "HT_PHASOR"
        return _function, 'Technical Analysis: HT_PHASOR', 'Meta Data'
