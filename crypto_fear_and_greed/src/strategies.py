from typing import Callable
import backtrader as bt
from .config import Config

class FearAndGreedStrategy(bt.Strategy):

    def __init__(self, duration: int, callback: Callable) -> None:
        self.duration = duration
        self.callback = callback
        # data
        self.order_date = None
        self.open = self.datas[0].open
        self.indicator = self.datas[1].value
        # value store
        self.val_start = self.broker.get_cash()  # keep the starting cash
        self.order_price = 0
        self.win = 0
        self.loose = 0

    def next(self):
        """
        Get the next day in the timeseries
        """
        if not self.position and self.indicator <= Config.threshold:
            size = int(self.broker.getcash() / self.open[0])
            self.buy(size=size)

        if (self.position and (
            self.datas[0].datetime.date(0) - self.order_date
        ).days > self.duration):
            self.close()

    def notify_order(self, order):
        """Calculate the roi of the trade
        and register win/loose

        Args:
            order (Any): The order details
        """

        if order.status in [order.Submitted, order.Accepted]:
            # An active Buy/Sell order has been submitted/accepted - Nothing to do
            return

        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
        if order.status in [order.Completed]:
            if order.isbuy():
                self.order_price = order.executed.price
                self.order_date = self.datas[0].datetime.date(0)
            elif order.issell():
                if self.order_price <= order.executed.price:
                    self.win += 1
                else:
                    self.loose += 1
            # Reset orders
            self.order = None

    def stop(self):
        """
        The end of our time series
        has been reached, print the result
        """
        trades = self.win + self.loose
        self.callback(self.win / trades if trades else 0)
