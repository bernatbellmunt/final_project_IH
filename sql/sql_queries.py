from sql_connection import engine
import pandas as pd

def get_all ():
    query = """SELECT * FROM prado_paintings;"""
    df = pd.read_sql_query(query, engine)
    return df

def get_img_from_artist (name):
    query = f"""SELECT * 
    FROM prado_paintings
    WHERE artist like '%{name}%';"""
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