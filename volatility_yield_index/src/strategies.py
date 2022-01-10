import backtrader as bt
from .config import Config

class BuyAndHoldIndexStrategy(bt.Strategy):
    def __init__(self):
        self.open = self.datas[0].open
        self.val_start = self.broker.get_cash()  # keep the starting cash
        self.open_trade = True

    def nextstart(self):
        # Buy all the available cash
        size = int(self.broker.getcash() / self.open[0])
        self.buy(size=size-10)

    def stop(self):
        # calculate the actual returns
        roi = (self.broker.get_value() / self.val_start) - 1.0
        print('Buy and Hold ROI: {:.2f}%'.format(100.0 * roi))
        print('{:.2f}% (annually)'.format(100.0 * roi / 18))

class IndexEtfStrategy(bt.Strategy):

    def __init__(self) -> None:
        # data
        self.open = self.datas[0].open
        self.vix = self.datas[1].vix_close
        self.vix_slope = self.datas[2].vix_slope
        self.t10y2y = self.datas[3].t10y2y
        self.t10y2y_slope = self.datas[4].t10y2y_slope
        # value store
        self.val_start = self.broker.get_cash()  # keep the starting cash
        self.order_price = 0
        self.win= 0
        self.loose= 0
        # flags
        self.t10y2y_bottom = False
        self.vix_peak = False

    def nextstart(self):
        # Buy all the available cash
        size = int(self.broker.getcash() / self.open[0])
        self.buy(size=size-10)

    def next(self):
        """
        Get the next day in the timeseries
        """
        if not self.vix_peak and self.vix[0] > Config.vix_threshold:
            self.vix_peak = True
        elif not self.t10y2y_bottom and self.t10y2y[0] < Config.t10y2y_threshold:
            self.t10y2y_bottom = True
        elif (not self.position 
            and self.vix_peak
            and self.vix_slope[0] <= Config.vix_slope_threshold):
            # indicator exceeded buy threshold
            size = int(self.broker.getcash() / self.open[0])
            self.buy(size=size)
        elif self.position and self.t10y2y_bottom and self.t10y2y_slope_cross():
            # indicator exceeded sell threshold
            self.close()
            self.t10y2y_bottom = False

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
            elif order.issell():
                if self.order_price <= order.executed.price:
                    self.win += 1
                else:
                    self.loose += 1
        # Reset orders
        self.order = None

    def t10y2y_slope_cross(self):
        return (self.t10y2y_slope[0] >= Config.t10y2y_slope_threshold 
                and self.t10y2y_slope[-1] <= Config.t10y2y_slope_threshold)

    def delta(self, old_value: float, new_value: float) -> float:
        """Get the price change: ouput range = [0, 1]

        Parameters
        ----------
        old_value : float
            The value in the past
        new_value : float
            The current value

        Returns
        -------
        float
            The increase/decrease of the value
        """
        Δ = new_value - old_value
        return round(Δ / old_value, 3)

    def stop(self):
        """
        The end of our time series
        has been reached, print the result
        """
        trades = self.win + self.loose
        roi = (self.broker.get_value() / self.val_start) - 1.0
        print('Strategy Win Rate:', self.win / trades if trades else 0)
        print('Strategy ROI: {:.2f}%'.format(100.0 * roi))
        print('{:.2f}% (annually)'.format(100.0 * roi / 18))