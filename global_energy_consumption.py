""" Generate Energy Consumption and Renewable Energy graphics

Author: Lucas Torres Marques
Date: 13/05/2022
"""
import pandas as pd
from utils.energy_consumption_graph import create_consumption_graph
from utils.renewable_energy_graph import create_renewable_graph

# Pre-processing dataset
energy_consumption = pd.read_csv('data/global-energy-substitution.csv')
energy_consumption = energy_consumption.drop(['Entity', 'Code'], axis=1)
energy_consumption.columns = ['year', 'wind', 'oil', 'nuclear', 'hydro',
                              'biomass', 'other_renewables', 'biofuels',
                              'solar', 'coal', 'gas']
energy_consumption = energy_consumption.set_index('year').sort_index(axis=0)
energy_consumption['total'] = energy_consumption.sum(axis=1)
energy_consumption['renewable'] = energy_consumption[
    ['wind', 'hydro', 'biomass', 'biofuels', 'other_renewables', 'solar']].sum(axis=1)

# Creating graphics
create_consumption_graph(energy_consumption)
create_renewable_graph(energy_consumption)
