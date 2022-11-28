from sql.sql_connection import engine
import pandas as pd
import color_functions

def get_all ():
    query = """SELECT * FROM prado_paintings;"""
    df = pd.read_sql_query(query, engine)
    return df

def get_img_from_artist (name):
    query = f"""SELECT * 
    FROM prado_paintings
    WHERE artist LIKE '%' {name} '%';"""
    df = pd.read_sql_query(query, engine)
    return df

def get_img_by_years (first, last):
    query = f"""SELECT * 
    FROM prado_paintings
    WHERE year between {first} and {last};"""
    df = pd.read_sql_query(query, engine)
    return df

def get_img_from_artist_year (name, first, last):
    query = f"""SELECT * 
    FROM prado_paintings
    WHERE artist like '%{name}%' and year between {first} and {last};"""
    df = pd.read_sql_query(query, engine)
    return df

#hauré de passar les funcions de colors sobre el dataframe
def get_random_pic_artist (name):
    query = f"""SELECT *
    FROM prado_paintings
    WHERE artist like '%'{name}'%';"""
    df = pd.read_sql_query(query, engine)
    samp=  df.sample()
    return samp


def prova (name):
    query = f"""SELECT * 
    FROM prado_paintings
    WHERE artist like '%'{name}'%';"""
    df = pd.read_sql_query(query, engine)
    return df  


def get_random_in_years (first, last):
    query = f"""SELECT * 
    FROM prado_paintings
    WHERE year between {first} and {last};"""
    df = pd.read_sql_query(query, engine)
    
    return df