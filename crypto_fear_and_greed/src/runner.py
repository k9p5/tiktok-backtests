import backtrader as bt
from .csv_data_feeds import FearAndGreedDataFeed
from .strategies import FearAndGreedStrategy
from .config import Config
from .utils import default_colors


class Runner:
    plot = False
    results = {
        'duration': [],
        'rate': []
    }
    duration = 0

    def callback(self, rate):
        self.results['duration'].append(self.duration)
        self.results['rate'].append(rate)

    def execute_backtests(self):

        cerebro = bt.Cerebro()
        cerebro.broker.setcash(100E4)
        cerebro.adddata(bt.feeds.YahooFinanceCSVData(
            dataname='static/BTC-USD.csv'))
        cerebro.adddata(FearAndGreedDataFeed(dataname='static/BTC-FNGI.csv'))
        cerebro.addstrategy(
            FearAndGreedStrategy,
            duration=self.duration,
            callback=self.callback
        )
        cerebro.run()

        # plot
        if self.plot:
            if Config.darkmode:
                default_colors()
                cerebro.plot(loc='white')
            else:
                cerebro.plot()
