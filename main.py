import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import codecs
import os
import sql.sql_queries as esecuele
import color_functions
import seaborn as sns
import matplotlib as plt

#import sql.sql_queries 
import pandas as pd
import numpy as np
import color_functions
import webbrowser
import time

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
museum_study = st.container()




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

with dataset:
    st.header("""Museum study""")
    st.text("El Prado Museum has one of the largests collections of Barroque, meaning that most of the pieces of art where done \nduring the XVII century")
    df=pd.read_csv("datasets/prado_oil.csv")

    #fig = plt.figure(figsize=(10,10))
    sns.histplot(x=df.year, bins=50, fill=None)
    #st.pyplot(plt.gcf())
with museum_study:
    st.header("Oil Paintings study")
    tab1, tab2 = st.tabs(["🎨 Artist", "📆 Year Range"])
    with tab1:
        st.header("""Select your artist""")
        st.text("Select your artist to visualize a random painting and the palette used in the painting")
        # too long - st.text(f"This are the possible artists: \n {color_functions.get_all_artists()}")
        input_artist=st.text_input("Introduce artist name",value="Goya",type="default",label_visibility="visible")
        st.set_option('deprecation.showPyplotGlobalUse', False)
        obra = color_functions.get_random_from_artist(input_artist)
        title=obra["title"]
        st.text(title)
        st.pyplot(color_functions.plot_image(obra), clear_figure=False)
        st.text("Additionally, we can see the top 3 colors that are used by our artist")
        st.image(color_functions.get_top3_artist(input_artist),use_column_width=False)

    with tab2:
        st.header("""Select your year range""")
        st.text("Enter the year range in the following input boxes:")
        first=st.text_input("Introduce first year",value="1600",type="default",label_visibility="visible")
    
        last=st.text_input("Introduce last year",value="1610",type="default",label_visibility="visible")
        obra2 = color_functions.get_random_from_years(int(first), int(last))
        title2=obra2["title"]
        artist2 = obra2["artist"]
        st.text(f"{title2} \n {artist2}")
        st.pyplot(color_functions.plot_image(obra2), clear_figure=False)
        st.text("Additionally, we can see the top 3 colors are used during this time range:")
        st.image(color_functions.get_top3_years(int(first), int(last)),use_column_width=False)



with st.sidebar:
# i will need to include the links to the different sections
    st.header("Welcome page")
    st.header("Methodology")
    st.header("Museum study")
    st.header("Oil paintings study")

#with methodology:

