import geopandas as gpd
import streamlit as st

from scripts import streamlit_funcs as stf
from scripts import file_reader as r

stf.set_page_config()

selected = stf.set_option_menu()
    
if selected == "Stations":
    stf.plot_stations(r.trains)

if selected == "Trains":
    pass

if selected == "About":
    stf.about()
