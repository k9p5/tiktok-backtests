from backtrader.feeds import GenericCSVData

class FearAndGreedDataFeed(GenericCSVData):

    lines = ('value', )

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
        ('value', 1),
        ('openinterest', -1),
    )