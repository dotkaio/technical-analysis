from functools import wraps
import requests
import inspect
import pandas
import re
import matplotlib as plt

class Fetch(object):

    alpha_url = "https://www.alphavantage.co/query?"
    # include more api

    def __init__(self, output_format='pandas',
                 _error=True,
                 indexing_type='date'):

        self.key = '8SNLOC3ASFQNRMMH'
        self.headers = {}
        self.output_format = output_format
        self._error = _error
        self._append_type = True
        self.indexing_type = indexing_type

    @classmethod
    def _call_api_on_func(cls, func):
        """ before the request.get() """

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
        def _call_wrapper(self, *args, **kwargs):

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
            if 'json' in self.output_format.lower() or 'csv' in self.output_format.lower():
                oformat = self.output_format.lower()
            elif 'pandas' in self.output_format.lower():
                oformat = 'json'
            else:
                raise ValueError("Output format: {} not recognized, only json,"
                                 "pandas and csv are supported".format(
                                     self.output_format.lower()))
            apikey_parameter = "&apikey={}".format(self.key)
            if self._append_type:
                url = '{}{}&datatype={}'.format(url, apikey_parameter, oformat)
            else:
                url = '{}{}'.format(url, apikey_parameter)
            return self._handle_api_call(url), data_key, meta_data_key
        return _call_wrapper

    @classmethod
    def _output_format_sector(cls, func, override=None):

        @wraps(func)
        def _format_wrapper(self, *args, **kwargs):
            json_response, data_key, meta_data_key = func(
                self, *args, **kwargs)
            if isinstance(data_key, list):
                # Replace the strings into percentage
                data = {key: {k: self.percentage_to_float(v)
                              for k, v in json_response[key].items()} for key in data_key}
            else:
                data = json_response[data_key]
            # TODO: Fix orientation in a better way
            meta_data = json_response[meta_data_key]
            # Allow to override the output parameter in the call
            if override is None:
                output_format = self.output_format.lower()
            elif 'json' or 'pandas' in override.lower():
                output_format = override.lower()
            # Choose output format
            if output_format == 'json':
                return data, meta_data
            elif output_format == 'pandas':
                data_pandas = pandas.DataFrame.from_dict(data,
                                                         orient='columns')
                # Rename columns to have a nicer name
                col_names = [re.sub(r'\d+.', '', name).strip(' ')
                             for name in list(data_pandas)]
                data_pandas.columns = col_names
                return data_pandas, meta_data
            else:
                raise ValueError('Format: {} is not supported'.format(
                    self.output_format))
        return _format_wrapper

    @classmethod
    def _output_format(cls, func, override=None):

        @wraps(func)
        def _format_wrapper(self, *args, **kwargs):
            call_response, data_key, meta_data_key = func(
                self, *args, **kwargs)
            if 'json' in self.output_format.lower() or 'pandas' \
                    in self.output_format.lower():
                data = call_response[data_key]

                if meta_data_key is not None:
                    meta_data = call_response[meta_data_key]
                else:
                    meta_data = None
                # Allow to override the output parameter in the call
                if override is None:
                    output_format = self.output_format.lower()
                elif 'json' or 'pandas' in override.lower():
                    output_format = override.lower()
                # Choose output format
                if output_format == 'json':
                    return data, meta_data
                elif output_format == 'pandas':
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

                    if 'integer' in self.indexing_type:
                        data_pandas.reset_index(level=0, inplace=True)
                        data_pandas.index.name = 'index'
                    else:
                        data_pandas.index.name = 'date'
                        data_pandas.index = pandas.to_datetime(
                            data_pandas.index)
                    return data_pandas, meta_data
            elif 'csv' in self.output_format.lower():
                return call_response, None
            else:
                raise ValueError('Format: {} is not supported'.format(
                    self.output_format))
        return _format_wrapper

    def _handle_api_call(self, url):

        response = requests.get(url, headers=self.headers)
        if 'json' in self.output_format.lower() or 'pandas' in \
                self.output_format.lower():
            json_response = response.json()
            if not json_response:
                raise ValueError(
                    'Error getting data from the api, no return was given.')
            elif "Error Message" in json_response:
                raise ValueError(json_response["Error Message"])
            elif "Information" in json_response and self._error:
                raise ValueError(json_response["Information"])
            elif "Note" in json_response and self._error:
                raise ValueError(json_response["Note"])
            return json_response
