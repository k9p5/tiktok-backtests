import pandas as pd
import numpy as np
from src.runner import Runner


runner = Runner()

runner.duration = 20
runner.plot = True
runner.execute_backtests()