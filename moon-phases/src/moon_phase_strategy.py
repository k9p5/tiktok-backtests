import backtrader as bt
from datetime import datetime
from typing import Callable
from .utils import delta, phase


class MoonPhaseStrategy(bt.Strategy):

    def __init__(self, result_callback: Callable[[float], None]):
        self.roi = 0
        self.order_price = 0
        self.result_callback = result_callback

    def next(self):
        _date = self.datas[0].datetime
        today = datetime(
            year=_date.date(0).year, 
            month=_date.date(0).month,
            day=_date.date(0).day,
        )
        yesterday = datetime(
            year=_date.date(-1).year, 
            month=_date.date(-1).month,
            day=_date.date(-1).day,
        )
        try:
            assert today > yesterday # not the case at index 0
            p1 = phase(today)
            p2 = phase(yesterday)
            if p1 == 'Full Moon' and p2 != 'Full Moon':
                self.buy() # enter long
            if p1 == 'New Moon' and p2 != 'New Moon':
                self.close() # close long position
        except:
            pass

            

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
