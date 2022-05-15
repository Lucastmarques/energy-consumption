"""Create an App to visualize data

Author: Lucas Torres Marques
Date: 15/05/2022
"""
import streamlit as st

st.title("""Data Visualization""")

st.caption("Lucas Torres Marques, 15 May 2022")

st.write("""
         ## Energy Consumption and Technological Development
         How world's energy consumption have been directly connected
         to technological development.""")
st.image('pictures/energy_consumption.png')
st.caption("""Source: [Our World in Data](https://ourworldindata.org/grapher/global-primary-energy?country=~OWID_WRL)""")

st.write("""
         ## Energy Sustainability
         How world's energy consumption is on the way to full
         production of renewable energy, and how it can break
         the idea that technogical development will forever be
         directly connected to technogical development.""")
st.image('pictures/sustainable_energy.png')
st.caption("""Source: [Our World in Data](https://ourworldindata.org/grapher/transistors-per-microprocessor?yScale=linear)""")

st.write("""You can access the [GitHub Repository](https://github.com/Lucastmarques/energy-consumption) to see more about the project.""")
