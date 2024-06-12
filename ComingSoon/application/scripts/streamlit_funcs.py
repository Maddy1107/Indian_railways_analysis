import streamlit as st
from streamlit_option_menu import option_menu

import geopandas as gpd
import plotly.express as px

def set_page_config():
    st.set_page_config(
        page_title="Indian Railways",
        page_icon="assets/icon.png",
        layout="wide",
    )

def set_option_menu():
    selected = option_menu(
        None,
        options=["Stations", "Trains", "About"],
        icons=["house-fill", "train-freight-front-fill", "person-fill"],
        menu_icon="cast",  # optional
        default_index=0,  # optional
        orientation="horizontal",
        styles={
            "container": {
                "padding": "0!important",
                "background-color": "#391c59",
                "width": "100%",
            },
            "icon": {"color": "yellow", "font-size": "20px"},
            "nav-link": {
                "font-face": "bold",
                "font-size": "20px",
                "text-align": "center",
                "margin": "0px",
                "--hover-color": "magenta",
            },
            "nav-link-selected": {"background-color": "#c25857"},
        },
    )
    return selected
    
def plot_stations(trains):
    st.write(trains)

def about():
    st.markdown(
        "## :blue[Project Title] : Geo-Visualization of Indian railways using Streamlit and Plotly"
    )
    st.markdown("## :blue[Technologies used] : Python, Plotly, JSON, Streamlit")
    st.markdown(
        "## :blue[Overview] : "
        "Retrieving the data from the JSON file,"
        "Change trains and station to geopandas dataframe with map geometry,"
        "Plot the data on map of india"
    )
