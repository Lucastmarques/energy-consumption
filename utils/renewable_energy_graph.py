""" Generate renewable energy graph

Author: Lucas Torres Marques
Date: 13/05/2022
"""
from typing import Union
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

def get_relation(test: Union[np.array, float, int],
                 true: Union[np.array, float, int]) -> Union[np.array, float]:
    """Calculate Relation between two given numbers
    Args:
        test (Union[np.array, float, int]): variable to get relation
        true (Union[np.array, float, int]): true value to compare
    Returns:
        Union[np.array, float]: absolute relation between two values
    """
    return abs(test - true) / true


def create_renewable_graph(data: pd.DataFrame):
    """Create Renewable Energy Graph
    Args:
            data (pd.DataFrame): energy consumption dataframe
    Returns:
            (None)
    Graph will be saved as a figure named as'renewable_energy_graph.png'
    """
    total_consumption = data['total']
    renewable_consumption = data['renewable']
    renewable_consumption[1945] = (
        renewable_consumption[1940] + renewable_consumption[1950]) / 2
    total_consumption[1945] = (
        total_consumption[1940] + total_consumption[1950]) / 2
    total_consumption = total_consumption.sort_index()
    renewable_consumption = renewable_consumption.sort_index()

    style.use('fivethirtyeight')

    _, axs = plt.subplots(4, 1, figsize=(9, 12))

    graph_color = '#ffbb47'

    for ax_subplots in axs:
        ax_subplots.plot(data.index, data['total'],
                color=graph_color, zorder=0, alpha=0.3, lw=3)
        ax_subplots.grid(False)
        ax_subplots.set_xlim(1919, 2019)
        ax_subplots.set_xticklabels([])
        ax_subplots.set_yticklabels([])

    # Emphasize 25 years for each graph
    axs[0].plot(total_consumption.index[:16], total_consumption[:16],
                color=graph_color, zorder=0)
    axs[1].plot(total_consumption.index[15:24], total_consumption[15:24],
                color=graph_color, zorder=0)
    axs[2].plot(total_consumption.index[23:49], total_consumption[23:49],
                color=graph_color, zorder=0)
    axs[3].plot(total_consumption.index[48:], total_consumption[48:],
                color=graph_color, zorder=0)

    # Energy Consumption values
    min_max_years = [
        [1920, 1945],
        [1945, 1970],
        [1970, 1995],
        [1995, 2019]
    ]
    rotation_dict = {"1920": 3, "1945": 15, "1970": 20, "1995": 25}
    y_var_offset = {
        "1920": -25000,
        "1945": -38000,
        "1970": -38000,
        "1995": -41000}
    x_var_offset = {"1920": -6, "1945": -5, "1970": -6, "1995": -6}
    renewable_xmin = 0.08
    renewable_xmax = 0.28
    renewable_xmax_dict = {
        "1920": 1 - get_relation(renewable_consumption[renewable_consumption.index[:16]].sum(),
                                 renewable_consumption.sum()),
        "1945": 1 - get_relation(renewable_consumption[renewable_consumption.index[15:24]].sum(),
                                 renewable_consumption.sum()),
        "1970": 1 - get_relation(renewable_consumption[renewable_consumption.index[23:49]].sum(),
                                 renewable_consumption.sum()),
        "1995": 1 - get_relation(renewable_consumption[renewable_consumption.index[48:]].sum(),
                                 renewable_consumption.sum()),
    }

    for ax_subplots, [year_min, year_max] in zip(axs, min_max_years):
        # year_max and year_min energy consumption
        ax_subplots.text(year_max - 3, total_consumption[year_max] + 8300,
                f'{int(total_consumption[year_max]/1000)}k',
                fontsize=10, color='grey')
        ax_subplots.text(year_min - 3, total_consumption[year_min] + 8300,
                f'{int(total_consumption[year_min]/1000)}k',
                fontsize=10, color='grey')

        # Delta
        var_x = (year_max + year_min) / 2
        var_y = (total_consumption[year_max] + total_consumption[year_min]) / 2
        var = get_relation(total_consumption[year_max], total_consumption[year_min])
        ax_subplots.text(var_x + x_var_offset[str(year_min)],
                var_y + y_var_offset[str(year_min)],
                f'\u0394 = {round(var*100, 1)}%',
                rotation=rotation_dict[str(year_min)],
                color='grey',
                fontsize=12)

        # Renewable bars
        renewable_color = '#14342B'
        relation = renewable_xmax_dict[str(year_min)]
        ax_subplots.axhline(
            100000,
            xmin=renewable_xmin,
            xmax=renewable_xmin +
            0.2 *
            relation,
            lw=7,
            color=renewable_color)
        ax_subplots.axhline(100000, xmin=renewable_xmin, xmax=renewable_xmax, lw=7,
                   color=renewable_color, alpha=0.3)
        x_pos = 1935 if round(relation * 100) < 10 else 1933
        ax_subplots.text(x_pos, 110000, f'{round(relation*100)}%',
                size=20, color=renewable_color, weight='bold')
        ax_subplots.text(1932, 85000, 'Renew. Energy',
                fontsize=8, color=renewable_color, alpha=0.6)

    # Title and subtitle
    axs[0].text(
        1918,
        235000,
        "Popularization of sustainable energy in the last 25 years",
        size=17,
        weight='bold')
    axs[0].text(
        1918,
        215000,
        "World energy consumption for the past 100 years in TWh for each 25 years")

    # Credits
    axs[-1].text(1917, -40000, 'Author: Lucas Torres Marques' + ' ' * 69 +
                 'Source: ourworldindata.org', color='#f0f0f0', backgroundcolor='#4d4d4d', size=12)

    # X-axis
    axs[-1].text(1917.5, -10000, '1919', fontsize=10, color='grey', alpha=0.6)
    axs[-1].text(1942.5, -10000, '1945', fontsize=10, color='grey', alpha=0.6)
    axs[-1].text(1967.5, -10000, '1970', fontsize=10, color='grey', alpha=0.6)
    axs[-1].text(1992.5, -10000, '1995', fontsize=10, color='grey', alpha=0.6)
    axs[-1].text(2016.5, -10000, '2019', fontsize=10, color='grey', alpha=0.6)

    plt.savefig('pictures/renewable_energy_graph.png')
    plt.show()
