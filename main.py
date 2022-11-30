import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import codecs
import os
import sql.sql_queries as esecuele
import color_functions
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import plotly.express as px
#import sql.sql_queries 
import pandas as pd
import numpy as np
import color_functions
import webbrowser
import time
from PIL import Image, ImageDraw

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
museum_study = st.container()
oil_painting_study = st.container()




with header:
    st.title("Welcome to El Prado Museum")

cover = Image.open("images/prado_gallery.jpeg")

with subheader:
    st.image(cover, use_column_width=False)
    st.header("""This is my final project in which I will analyze the color palettes that are used in pieces of art.""")


with methodology:
    st.header("""Methodology""")
    url = "https://www.museodelprado.es/en/the-collection/art-works"
    st.markdown("The goal of my project is to study the color palettes used by artists and time periods. In order to get the images from the oil paintings from El Prado Museum I have scraped the following webiste using Selenium.")
    if st.button('Prado Collection Website'):
        webbrowser.open_new_tab(url)
    st.markdown("The Prado Museum has a large register of pieces of art, between which there are sculptures, frescos and oil paintings.")
    st.markdown("After some cleaning, the resulting dataframe, that has been loaded to MySQL Workbench is the following:")
    taxi_data = pd.read_csv("datasets/prado.csv")
    st.write(taxi_data.head())
    st.markdown("This CSV file contains all the registers from El Prado, but I will create a second dataset for all oil paintings. This new subset will be the one used in my analysis.")
    taxi_data = pd.read_csv("datasets/prado_oil.csv")
    st.write(taxi_data.head())
    st.markdown("My code is structured in different document, all of the .py documents.")
    st.markdown("main.py contains all the streamlit page code and color_functions.py contains all the functions that render palettes and that will be used in my page.")

with museum_study:
    st.header("""Museum study""")
    st.markdown("El Prado Museum has one of the largests collections of Barroque, meaning that most of the pieces of art where done during the XVII century.")
    df=pd.read_csv("datasets/prado_oil.csv")

    fig=plt.figure(figsize=(5, 5))
    
    ax1 = fig.add_subplot(1,1,1)
    sns.histplot(x=df.year, bins=50, fill=None)
    
    ax1.set_xlabel("Years")
    ax1.set_ylabel("Oil Paintings")
    ax1.set_title("Distribution of paintings by years")
    ax1.grid(False)
    ax1.set_facecolor((1, 1, 1))
    ax1.set_frame_on(True)
    
    fig.savefig("images/graph1.jpg")
    graph1 =  Image.open("images/graph1.jpg")
    graph1 = graph1.resize((700, 700))
    st.image(graph1, use_column_width=False)

    st.markdown("The representation of painters in el Prado Museum, ignoring the pieces of art that are catalogued as anonymous, is the following:")
    graph2 =  Image.open("images/graph2.jpg")
    graph2 = graph2.resize((700, 700))
    st.image(graph2, use_column_width=False)

with oil_painting_study:
    st.header("Oil Paintings study")
    tab1, tab2 = st.tabs(["🎨 Artist", "📆 Year Range"])
    with tab1:
        st.header("""Select your artist""")
        st.markdown("Select your artist to visualize a random painting and the palette used in the painting")
        # too long - st.text(f"This are the possible artists: \n {color_functions.get_all_artists()}")
        input_artist=st.text_input("Introduce artist name",value="Goya",type="default",label_visibility="visible")
        st.set_option('deprecation.showPyplotGlobalUse', False)
        obra = color_functions.get_random_from_artist(input_artist)
        title=obra["title"]
        st.markdown(title)
        st.pyplot(color_functions.plot_image(obra), clear_figure=False)
        st.markdown("Additionally, we can see the top 3 colors that are used by our artist")
        st.image(color_functions.get_top3_artist(input_artist),use_column_width=False)

    with tab2:
        st.header("""Select your year range""")
        st.markdown("Enter the year range in the following input boxes:")
        first=st.text_input("Introduce first year",value="1500",type="default",label_visibility="visible")
    
        last=st.text_input("Introduce last year",value="1510",type="default",label_visibility="visible")
        obra2 = color_functions.get_random_from_years(int(first), int(last))
        title2=obra2["title"]
        artist2 = obra2["artist"]
        st.markdown(f"{title2} \n {artist2}")
        st.pyplot(color_functions.plot_image(obra2), clear_figure=False)
        st.markdown("Additionally, we can see the top 3 colors are used during this time range:")
        st.image(color_functions.get_top3_years(int(first), int(last)),use_column_width=False)
        st.markdown("In order to get the main color for each year, you can enter the year and the main color will appear:")
        input=st.text_input("Introduce the year in order to obtain main color used in that year:",value="1601",type="default",label_visibility="visible")
        color_code = color_functions.return_main_color(int(input))
        st.markdown(f"For the year selected the main color code is the following:{color_code}")
        result = Image.new("RGBA", (100, 100), (0, 0, 0, 0))
        canvas = ImageDraw.Draw(result)
        canvas.rectangle([(100, 100), (1, 1)], fill=color_code)
        st.image(result, use_column_width=False)





with st.sidebar:
# i will need to include the links to the different sections
    st.header("Welcome")
    st.header("Methodology")
    st.header("Museum study")
    st.header("Oil paintings study")



