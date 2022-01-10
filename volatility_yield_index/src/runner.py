import matplotlib
import matplotlib.pyplot as plt
import backtrader as bt
from .csv_data_feeds import (
    VixDataFeed,
    VixSlopeDataFeed,
    T10Y2YDataFeed,
    T10Y2YSlopeDataFeed
)
from .strategies import (
    IndexEtfStrategy,
    BuyAndHoldIndexStrategy
)
from .config import Config

SIZE = 6
COLOR = 'white'
BACKGROUND = "black"
GRID="0.4"

class Runner:

    def default_colors(
            self,
            color:str=COLOR,
            size:str=SIZE,
            background:str=BACKGROUND,
            grid:str=GRID
        ) -> None:
        matplotlib.use('Agg')
        plt.style.use('fivethirtyeight')
        #plt.style.use('dark_background')
        plt.rcParams["figure.figsize"] = (10, 6)
        plt.rcParams['lines.linewidth'] = 0.2
        plt.rcParams['lines.color']="0.5"
        plt.rcParams['patch.edgecolor']="white"
        
        plt.rcParams["font.size"] = size
        plt.rcParams['axes.labelsize'] = size
        plt.rcParams['ytick.labelsize'] = size
        plt.rcParams['xtick.labelsize'] = size

        plt.rcParams['text.color'] = color
        plt.rcParams['axes.labelcolor'] = color
        plt.rcParams['xtick.color'] = color
        plt.rcParams['ytick.color'] = color
        
        plt.rcParams['axes.grid.axis']='both'
        plt.rcParams['grid.linewidth']=0.1
        plt.rcParams['grid.color']=grid
        plt.rcParams['axes.linewidth']=0
        
        plt.rcParams['figure.facecolor'] = background
        plt.rcParams['axes.facecolor'] = background
        plt.rcParams["savefig.dpi"]=120
        dpi = plt.rcParams["savefig.dpi"]
        width = 700
        height = 1200
        plt.rcParams['figure.figsize'] = height/dpi, width/dpi
        plt.rcParams["savefig.facecolor"] = background
        plt.rcParams["savefig.edgecolor"] = background
        
        plt.rcParams['legend.fontsize'] = SIZE + 2
        plt.rcParams['legend.title_fontsize'] = SIZE + 2
        plt.rcParams['legend.labelspacing'] = 0.25
        plt.rcParams['image.cmap']='tab10'
        
        plt.ioff()

    def execute_backtests(self):

        cerebro = bt.Cerebro()
        cerebro.broker.setcash(100E3)
        cerebro.broker.setcommission(commission=0.005) # 0.5% of the operation value
        cerebro.adddata(bt.feeds.YahooFinanceCSVData(dataname='static/SPY.csv'))
        cerebro.adddata(VixDataFeed(dataname='static/VIX.csv'))
        cerebro.adddata(VixSlopeDataFeed(dataname='static/VIX_SLOPE.csv'))
        cerebro.adddata(T10Y2YDataFeed(dataname='static/T10Y2Y.csv'))
        cerebro.adddata(T10Y2YSlopeDataFeed(dataname='static/T10Y2Y_SMA_SLOPE.csv'))
        cerebro.addstrategy(IndexEtfStrategy)
        #cerebro.addstrategy(BuyAndHoldIndexStrategy)
        cerebro.run()

        # plot
        if Config.darkmode:
            self.default_colors()
            cerebro.plot(loc='white')
        else:
            cerebro.plot()
