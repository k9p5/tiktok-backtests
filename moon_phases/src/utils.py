import os
from typing import Union, Tuple
from datetime import datetime
from twelvedata import TDClient


def delta(old_value: float, new_value: float) -> float:
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


def get_data_path(
        symbol: str,
        start: Union[datetime, Tuple[datetime]],
        end: Union[datetime, Tuple[datetime]],
        interval="1day",
        outputsize=5000) -> str:
    """Get the path where the OHLC dataset
    has been saved for the specified
    arguments 

    export TWELVE_DATA_API_KEY=XXX 
    required

    Parameters
    ----------
    symbol : str
        Identifier like AAPL
    start : Union[datetime, Tuple[datetime]]
        First datetime that should be included
    end : Union[datetime, Tuple[datetime]]
        Last datetime that should be included
    interval : str, optional
        Tick duration like 1min, 15min, by default "1day"
    outputsize : int, optional
        How many rows should be included, by default 5000

    Returns
    -------
    str
        Path to the csv
    """

    td = TDClient(apikey=os.environ['TWELVE_DATA_API_KEY'])

    # Construct the necessary time series
    ts = td.time_series(
        symbol=symbol,
        interval=interval,
        outputsize=outputsize,
        start_date=start,
        end_date=end,
    )


    # Returns pandas.DataFrame
    df = ts.as_pandas()

    assert df is not None

    path = f'./{symbol.replace("/", "_")}.csv'

    df[::-1].to_csv(path)

    return path
