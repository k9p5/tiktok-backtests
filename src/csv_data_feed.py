from backtrader.feeds import GenericCSVData


class CSVDataFeed(GenericCSVData):
    params = (
        ('nullvalue', float('NaN')),
        ('dtformat', '%Y-%m-%d %H:%M:%S'),
        ('tmformat', '%H:%M:%S'),
        ('nullvalue', 0.0),
        ('datetime', 0),
        ('time', -1),
        ('open', 1),
        ('high', 2),
        ('low', 3),
        ('close', 4),
        ('volume', 5),
        ('openinterest', -1),
    )
