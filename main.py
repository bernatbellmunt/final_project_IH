import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import codecs
import sql.sql_connection
import sql.sql_queries
import pandas as pd
import numpy as np
import color_functions
import webbrowser

st.set_page_config(
     page_title="Prado Color Study",
     page_icon="🎨",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "This page has been created by Bernat Bellmunt. This is Bernat's final project at Ironhack!"
     }
 )




#this are the sections of my page!
header = st.container()
subheader = st.container()
methodology = st.container()
dataset = st.container()




with header:
    st.title("Welcome to El Prado Museum")

cover = Image.open("images/prado_gallery.jpeg")

with subheader:
    st.image(cover, use_column_width=False)
    st.header("""This is my final project in which I will analyze the color palettes that are used in pieces of art.""")


with methodology:
    st.header("""Methodology""")
    url = "https://www.museodelprado.es/en/the-collection/art-works"
    st.text("The goal of my project is to study the color palettes used by artists. In order to get the images from the oil paintings from\nEl Prado Museum I have scraped the following webiste using Selenium.")
    if st.button('Prado Collection Website'):
        webbrowser.open_new_tab(url)
    
    st.text("After some cleaning, the resulting dataframe, that has been loaded to MySQL Workbench is the following:")
    taxi_data = pd.read_csv("datasets/prado.csv")
    st.write(taxi_data.head())
    st.text("This CSV file contains all the registers from El Prado, but I will create a second dataset for all oil paintings.")
    taxi_data = pd.read_csv("datasets/prado_oil.csv")
    st.write(taxi_data.head())

with st.sidebar:

    st.header("Welcome page")
    st.header("Methodology")
    st.header("Museum study")
    st.header("Oil paintings study")

#with methodology:

