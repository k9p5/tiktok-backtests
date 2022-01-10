from datetime import datetime

class Config(object):
    sma_fast=21
    sma_slow=50
    sma_trend=200
    end_date = datetime(2021, 12, 31)
    start_date = datetime(2021, 1, 1)