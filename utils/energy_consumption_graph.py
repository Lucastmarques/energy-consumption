""" Generate energy consumption graph

Author: Lucas Torres Marques
Date: 13/05/2022
"""
import pandas as pd
from matplotlib import style
import matplotlib.pyplot as plt

def create_consumption_graph(data: pd.DataFrame):
    """ Create Energy Consumption Graph
    Args:
            data (pd.DataFrame): energy consumption dataframe
    Returns:
            (None)
    Graph will be saved as a figure named as 'energy_consumption.png'
    """
    style.use('fivethirtyeight')

    _, ax_subplot = plt.subplots(figsize=(9,5))

    ax_subplot.plot(data.index, data['total'],
            color='#ffbb47', zorder=0)
    ax_subplot.grid(False)
    xlim_max = data.index[-1]
    xlim_min = xlim_max - 100
    ax_subplot.set_xlim(xlim_min, xlim_max)
    ax_subplot.set_xticklabels([])
    ax_subplot.set_yticklabels([])

    # WWII and Cold War enclosures
    ax_subplot.axhline(data['total'][xlim_max], xmin=0.2, xmax=0.263,
                       color='grey', alpha=0.1, lw=510)
    ax_subplot.text(1942.5, 140000, 'World War II', fontsize=12, weight='bold',
            color='grey', alpha=0.3, rotation=90)
    ax_subplot.axhline(200000, xmin=0.28, xmax=0.723, color='grey', alpha=0.1, lw=510)
    ax_subplot.text(1988.5, 157500, 'Cold War', fontsize=12, weight='bold',
            color='grey', alpha=0.3, rotation=90)

    # X-axis
    ax_subplot.axhline(10000, xmin=0, xmax=1, color='grey', alpha=0.6, lw=1)
    ax_subplot.text(1917.5, 0, '1919', fontsize=10, color='grey', alpha=0.6)
    ax_subplot.text(1936.5, 0, '1939', fontsize=10, color='grey', alpha=0.6)
    ax_subplot.text(1944.5, 0, '1947', fontsize=10, color='grey', alpha=0.6)
    ax_subplot.text(1988.5, 0, '1991', fontsize=10, color='grey', alpha=0.6)
    ax_subplot.text(2016.5, 0, '2019', fontsize=10, color='grey', alpha=0.6)

    # 100,000 TWh support line
    ax_subplot.axhline(100000, xmin=0, xmax=1, color='grey', alpha=0.2, lw=1)
    ax_subplot.text(2014, 101500, '100K', fontsize=10, color='grey', alpha=0.6)

    # Title and subtitle
    ax_subplot.text(1918,235000,"Energy Consumption is Increased by Technological Development",
            size=17, weight='bold')
    ax_subplot.text(1918,222000,"World energy consumption for the past 100 years in TWh")

    # Credits
    ax_subplot.text(1917, -20000,
                    'Author: Lucas Torres Marques' + ' '*69 + 'Source: ourworldindata.org',
                    color = '#f0f0f0', backgroundcolor = '#4d4d4d', size=12)

    # Important things in technology history
    points_color = '#414535'

    # Television Invention
    ax_subplot.scatter([1926], 19900, color=points_color)
    ax_subplot.text(1920, 24050, 'Television', size=12, color=points_color, weight='bold')

    # First PC generation
    ax_subplot.scatter([1950], 28516, color=points_color)
    ax_subplot.text(1942, 34000, 'First PC', size=12, color=points_color, weight='bold')

    # Internet invention
    ax_subplot.scatter([1966], 54791, color=points_color)
    ax_subplot.text(1966, 43000, 'Video Game', size=12, color=points_color, weight='bold')

    # Internet invention
    ax_subplot.scatter([1983], 88315, color=points_color)
    ax_subplot.text(1980, 75315, 'Internet', size=12, color=points_color, weight='bold')

    # iPhone invention
    ax_subplot.scatter([2007], 146574, color=points_color)
    ax_subplot.text(1999, 151000, 'iPhone', size=12, color=points_color, weight='bold')

    # Bitcoin invention
    ax_subplot.scatter([2009], 145881, color=points_color)
    ax_subplot.text(2009, 133000, 'Bitcoin', size=12, color=points_color, weight='bold')

    plt.savefig('pictures/energy_consumption.png')
    plt.show()
