import os
import time
import pandas as pd
import backtrader as bt
from typing import List
from datetime import datetime, timedelta
from .csv_data_feed import CSVDataFeed
from .golden_cross_strategy import GoldenCrossStrategy
from .utils import get_data_path


end_date = datetime.now()
start_date = datetime.now() - timedelta(days=365)
s_and_p_500 = pd.read_csv('s_and_p_500.csv')
results: List[float] = list()


def result_callback(result: float) -> None:
    results.append(result)


def test_symbol(symbol: str) -> None:

    # Create a cerebro entity
    cerebro = bt.Cerebro()

    try:
        path = get_data_path(symbol, start_date, end_date, interval="15min")
    except:
        print(f'{symbol} could not be retrieved')
        return

    # Add the Data Feed to Cerebro
    cerebro.adddata(CSVDataFeed(dataname=path))

    # Add a strategy
    cerebro.addstrategy(GoldenCrossStrategy, result_callback=result_callback)

    # Set our desired cash start
    cerebro.broker.setcash(2000.0)

    # Set the commission
    # cerebro.broker.setcommission(commission=0.001)

    # Run over everything
    cerebro.run()

    # Plot for debugging
    # cerebro.plot()

    os.remove(path)


def run_tests():
    for index, row in s_and_p_500.iterrows():
        test_symbol(str(row['Symbol']))
        print('.', end=" ")
        time.sleep(7)  # due to 12data rate limit
    print('\nThe Average Expected Return is: ', sum(results) / len(results))
