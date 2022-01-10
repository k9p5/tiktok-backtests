from datetime import datetime

class Config(object):
    end_date = datetime(2021,12,31) # or datetime.now()
    start_date = datetime(2019,1,1)
    symbols = ["BTC/USD"] # can be multiple
