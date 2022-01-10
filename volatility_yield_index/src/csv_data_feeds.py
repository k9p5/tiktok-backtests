from backtrader.feeds import GenericCSVData


class VixDataFeed(GenericCSVData):

    lines = ('vix_open', 'vix_high', 'vix_low', 'vix_close')
    
    params = (
        ('nullvalue', float('NaN')),
        ('dtformat', '%m/%d/%Y'),
        ('tmformat', '%H:%M:%S'),
        ('nullvalue', 0.0),
        ('datetime', 0),
        ('time', -1),
        ('vix_open', 1),
        ('vix_high', 2),
        ('vix_low', 3),
        ('vix_close', 4),
        ('volume', -1),
        ('openinterest', -1),
    )

class VixSlopeDataFeed(GenericCSVData):

    lines = ('vix_slope', )

    params = (
        ('nullvalue', float('NaN')),
        ('dtformat', '%m/%d/%Y'),
        ('tmformat', '%H:%M:%S'),
        ('nullvalue', 0.0),
        ('datetime', 0),
        ('time', -1),
        ('open', 1),
        ('high', 1),
        ('low', 1),
        ('close', 1),
        ('volume', -1),
        ('vix_slope', 1),
        ('openinterest', -1),
    )

class T10Y2YDataFeed(GenericCSVData):

    lines = ('t10y2y', )

    params = (
        ('nullvalue', float('NaN')),
        ('dtformat', '%Y-%m-%d'),
        ('tmformat', '%H:%M:%S'),
        ('nullvalue', 0.0),
        ('datetime', 0),
        ('time', -1),
        ('open', 1),
        ('high', 1),
        ('low', 1),
        ('close', 1),
        ('volume', -1),
        ('t10y2y', 1),
        ('openinterest', -1),
    )

class T10Y2YSlopeDataFeed(GenericCSVData):

    lines = ('t10y2y_slope', )

    params = (
        ('nullvalue', float('NaN')),
        ('dtformat', '%Y-%m-%d'),
        ('tmformat', '%H:%M:%S'),
        ('nullvalue', 0.0),
        ('datetime', 0),
        ('time', -1),
        ('open', 1),
        ('high', 1),
        ('low', 1),
        ('close', 1),
        ('volume', -1),
        ('t10y2y_slope', 1),
        ('openinterest', -1),
    )