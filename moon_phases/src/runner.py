import os
import backtrader as bt
from .csv_data_feed import CSVDataFeed
from .moon_phase_strategy import MoonPhaseStrategy
from .utils import get_data_path
from .config import Config

def test_symbol(symbol: str) -> None:

    # Create a cerebro entity
    cerebro = bt.Cerebro()

    try:
        data_path = get_data_path(
            symbol,
            Config.start_date,
            Config.end_date,
            interval="1day"
        )
    except:
        print(f'{symbol} could not be retrieved')
        return

    # Add the Data Feed to Cerebro
    cerebro.adddata(CSVDataFeed(dataname=data_path))

    # Add a strategy
    cerebro.addstrategy(
        MoonPhaseStrategy,
        result_callback=lambda res: print('Strategy Result:', res)
    )

    # Set our desired cash start
    cerebro.broker.setcash(2000000.0)

    # Set the commission
    # cerebro.broker.setcommission(commission=0.001)

    # Run over everything
    cerebro.run()

    if len(Config.symbols) == 1:
        cerebro.plot()

    os.remove(data_path)


def run_tests():
    """Test one or more symbols"""
    list(map(test_symbol, Config.symbols))
