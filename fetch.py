from functools import wraps
import requests, inspect, pandas, re

class Fetch(object):
    alpha_url = "https://www.alphavantage.co/query?"
    def __init__(self, outform='pandas', error=True, indexing='date'):
        self.key = '8SNLOC3ASFQNRMMH'
        self.headers = {}
        self.outform = outform
        self.error = error
        self.appending = True
        self.indexing = indexing
    @classmethod
    def api(cls, func):
        argspec = inspect.getfullargspec(func)
        try:
            positional_count = len(argspec.args) - len(argspec.defaults)
            defaults = dict(
                zip(argspec.args[positional_count:], argspec.defaults))
        except TypeError:
            if argspec.args:
                positional_count = len(argspec.args)
                defaults = {}
            elif argspec.defaults:
                positional_count = 0
                defaults = argspec.defaults
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            used_kwargs = kwargs.copy()
            used_kwargs.update(zip(argspec.args[positional_count:], args[positional_count:]))
            used_kwargs.update({k: used_kwargs.get(k, d) for k, d in defaults.items()})
            function_name, data_key, meta_data_key = func(self, *args, **kwargs)
            base_url = Fetch.alpha_url
            url = "{}function={}".format(base_url, function_name)
            for idx, arg_name in enumerate(argspec.args[1:]):
                try:
                    arg_value = args[idx]
                except IndexError:
                    arg_value = used_kwargs[arg_name]
                if 'matype' in arg_name and arg_value:
                    arg_value = self.map_to_matype(arg_value)
                if arg_value:
                    if isinstance(arg_value, tuple) or isinstance(arg_value, list):
                        arg_value = ','.join(arg_value)
                    url = '{}&{}={}'.format(url, arg_name, arg_value)
            if 'json' in self.outform.lower() or 'csv' in self.outform.lower():
                oformat = self.outform.lower()
            elif 'pandas' in self.outform.lower():
                oformat = 'json'
            else:
                raise ValueError("Output format: {} not recognized, only json,"
                                 "pandas and csv are supported".format(
                                     self.outform.lower()))
            apikey_parameter = "&apikey={}".format(self.key)
            if self.appending:
                url = '{}{}&datatype={}'.format(url, apikey_parameter, oformat)
            else:
                url = '{}{}'.format(url, apikey_parameter)
            return self.api_call(url), data_key, meta_data_key
        return wrapper
    @classmethod
    def sector(cls, func, override=None):
        @wraps(func)
        def wrapper_format(self, *args, **kwargs):
            json_response, data_key, meta_data_key = func(
                self, *args, **kwargs)
            if isinstance(data_key, list):
                data = {key: {k: self.percentage_to_float(v)
                              for k, v in json_response[key].items()} for key in data_key}
            else:
                data = json_response[data_key]
            meta_data = json_response[meta_data_key]
            # Allow to override the output parameter in the call
            if override is None:
                outform = self.outform.lower()
            elif 'json' or 'pandas' in override.lower():
                outform = override.lower()
            # Choose output format
            if outform == 'json':
                return data, meta_data
            elif outform == 'pandas':
                data_pandas = pandas.DataFrame.from_dict(data,
                                                         orient='columns')
                col_names = [re.sub(r'\d+.', '', name).strip(' ')
                             for name in list(data_pandas)]
                data_pandas.columns = col_names
                return data_pandas, meta_data
            else:
                raise ValueError('Format: {} is not supported'.format(
                    self.outform))
        return wrapper_format
    @classmethod
    def outform(cls, func, override=None):
        @wraps(func)
        def wrapper_format(self, *args, **kwargs):
            call_response, data_key, meta_data_key = func(
                self, *args, **kwargs)
            if 'json' in self.outform.lower() or 'pandas' \
                    in self.outform.lower():
                data = call_response[data_key]
                if meta_data_key is not None:
                    meta_data = call_response[meta_data_key]
                else:
                    meta_data = None
                if override is None:
                    outform = self.outform.lower()
                elif 'json' or 'pandas' in override.lower():
                    outform = override.lower()
                if outform == 'json':
                    return data, meta_data
                elif outform == 'pandas':
                    if isinstance(data, list):
                        data_array = []
                        for val in data:
                            data_array.append([v for _, v in val.items()])
                        data_pandas = pandas.DataFrame(data_array, columns=[
                            k for k, _ in data[0].items()])
                    else:
                        try:
                            data_pandas = pandas.DataFrame.from_dict(data, orient='index', dtype='float')
                        except ValueError:
                            data = {data_key: data}
                            data_pandas = pandas.DataFrame.from_dict(data, orient='index', dtype='object')
                            return data_pandas, meta_data
                    if 'integer' in self.indexing:
                        data_pandas.reset_index(level=0, inplace=True)
                        data_pandas.index.name = 'index'
                    else:
                        data_pandas.index.name = 'date'
                        data_pandas.index = pandas.to_datetime(
                            data_pandas.index)
                    return data_pandas, meta_data
            elif 'csv' in self.outform.lower():
                return call_response, None
            else:
                raise ValueError('Format: {} is not supported'.format(
                    self.outform))
        return wrapper_format
    def api_call(self, url):
        response = requests.get(url, headers=self.headers)
        if 'json' in self.outform.lower() or 'pandas' in \
                self.outform.lower():
            json_response = response.json()
            if not json_response:
                raise ValueError(
                    'Error getting data from the api, no return was given.')
            elif "Error Message" in json_response:
                raise ValueError(json_response["Error Message"])
            elif "Information" in json_response and self.error:
                raise ValueError(json_response["Information"])
            elif "Note" in json_response and self.error:
                raise ValueError(json_response["Note"])
            return json_response
