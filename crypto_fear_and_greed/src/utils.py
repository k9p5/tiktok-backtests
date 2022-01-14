import matplotlib
import matplotlib.pyplot as plt

SIZE = 6
COLOR = 'white'
BACKGROUND = "#101622"
GRID = "0.4"


def default_colors(
    color: str = COLOR,
    size: str = SIZE,
    background: str = BACKGROUND,
    grid: str = GRID
) -> None:
    matplotlib.use('Agg')
    plt.style.use('fivethirtyeight')
    # plt.style.use('dark_background')
    plt.rcParams["figure.figsize"] = (10, 6)
    plt.rcParams['lines.linewidth'] = 0.05
    plt.rcParams['lines.color'] = "0.5"
    plt.rcParams['patch.edgecolor'] = "white"

    plt.rcParams["font.size"] = size
    plt.rcParams['axes.labelsize'] = size
    plt.rcParams['ytick.labelsize'] = size
    plt.rcParams['xtick.labelsize'] = size

    plt.rcParams['text.color'] = color
    plt.rcParams['axes.labelcolor'] = color
    plt.rcParams['xtick.color'] = color
    plt.rcParams['ytick.color'] = color

    plt.rcParams['axes.grid.axis'] = 'both'
    plt.rcParams['grid.linewidth'] = 0.1
    plt.rcParams['grid.color'] = grid
    plt.rcParams['axes.linewidth'] = 0

    plt.rcParams['figure.facecolor'] = background
    plt.rcParams['axes.facecolor'] = background
    plt.rcParams["savefig.dpi"] = 120
    dpi = plt.rcParams["savefig.dpi"]
    width = 700
    height = 1200
    plt.rcParams['figure.figsize'] = height/dpi, width/dpi
    plt.rcParams["savefig.facecolor"] = background
    plt.rcParams["savefig.edgecolor"] = background

    plt.rcParams['legend.fontsize'] = SIZE + 2
    plt.rcParams['legend.title_fontsize'] = SIZE + 2
    plt.rcParams['legend.labelspacing'] = 0.25
    plt.rcParams['image.cmap'] = 'tab10'

    plt.ioff()
