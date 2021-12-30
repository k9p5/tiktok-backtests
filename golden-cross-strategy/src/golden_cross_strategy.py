import backtrader as bt
from typing import Callable
from .utils import (
    delta,
    max_delta,
    crossed
)


class GoldenCrossStrategy(bt.Strategy):
    # list of parameters which are configurable for the strategy
    params = dict(
        pfast=21,  # period for the fast moving average
        pslow=50,  # period for the slow moving average
        ptrend=200   # trend moving average
    )

    def __init__(self, result_callback: Callable[[float], None]):
        self.sma1 = bt.ind.SMA(period=self.p.pfast)  # fast moving average
        self.sma2 = bt.ind.SMA(period=self.p.pslow)  # slow moving average
        self.sma3 = bt.ind.SMA(period=self.p.ptrend)  # slow moving average
        self.roi = 0
        self.order_price = 0
        self.result_callback = result_callback

    def next(self):
        if not self.position:  # not in the market
            if crossed(self.sma1, self.sma2):  # if fast crosses slow to the upside
                self.buy()  # enter long

        elif max_delta(self.sma1, self.sma2):  # in the market & cross to the downside
            self.close()  # close long position

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # An active Buy/Sell order has been submitted/accepted - Nothing to do
            return

        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
        if order.status in [order.Completed]:
            if order.isbuy():
                self.order_price = order.executed.price
            elif order.issell():
                self.roi += delta(self.order_price, order.executed.price)

        # Reset orders
        self.order = None

    def stop(self):
        self.result_callback(self.roi)
