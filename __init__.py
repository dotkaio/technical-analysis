""" hello there, kaio here...

    this module is a wrapper for the 'https://alhavantage.co' API.
    I'll be including others APIs, like Oanda, Ninjatrader, etc.

    If you want to get more information, please visit
    'https://www.alphavantage.co/documentation'.

    Until now we have a solid way to fetch data from the alphavantage API. I've
    also implement a graphical representation of the data using matplotlib. But
    right now i'm more focus on finish the strategy I started, which include
    verify for preveius cross average, and start to watch for fibonacci
    retracenments within 15min, 5min timeframe. Just saying...

    I'm not really a good trader, but if you do have a strategy and want me to
    implement, let me know.

    There is a lot of docstrings missing, but don't worry, after it is done, I
    can start including more information about it.  """

from .fetch import Fetch
from .indicator import Indicator
from .crypto import Crypto
from .ticker import Ticker
from .forex import Forex
