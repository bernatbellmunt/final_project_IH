# All functions are stored in this file - we will call this file from the others


#imports
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from bs4 import BeautifulSoup
import re as re
import time
import pandas as pd
import os
import numpy as np
import requests
import pymysql
import sqlalchemy as alch
from getpass import getpass

import googletrans
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import spacy



#this first function returns me the html from el prado -> with selenium
def get_html (url):
    import os

    url = "https://www.museodelprado.es/en/the-collection/art-works"

    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    #options.add_argument("--headless")

    driver = webdriver.Chrome(options = options)
    driver.get(url)

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))).click()

    #start = time.time()
    driver.execute_script("document.querySelector('footer').style.display = 'None'")


    #elemento = "document.querySelector('mostrable miniaturas')"
    #buscador-coleccion-resultados



    last_height = driver.execute_script("return document.body.scrollHeight")
    html = driver.execute_script("return document.body.outerHTML;")
    soup = BeautifulSoup(html, "html.parser")
    total_number = soup.find_all("strong", {"id":"panNumResultados"})[0]
    a=total_number.text
    total_number=int(re.findall("\d{4}",a)[0])

    while len(get_image_list(html)) < total_number:
        #driver.execute_script("document.querySelector('footer').style.display = 'None'")
        driver.execute_script(f"window.scrollBy(0, {last_height});")

        time.sleep(5)
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break
        last_height = new_height

    html = driver.execute_script("return document.body.outerHTML;")
    print(len(html))
    os.system("say -v monica ayamdon")
    return html



#Functions -> scraping the html!!!!!!!

#title
def get_title(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    word="dt"

    tags = soup.find_all(word)
    titles=[c.getText().replace(">", "").strip() for c in tags]
    #the first 44 items are from the menu -> we don't want this, then, titles are duplicated!!!!
    titles = titles[44:]
    newtitles=[]
    i=0
    while i < len(titles):
        newtitles.append(titles[i])
        i+=2
    return newtitles

#subtitle
def get_subtitle(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    word="dd"

    tags = soup.find_all(word, attrs={"class":"soporte"})
    subtitles=[c.getText().replace(">", "").strip() for c in tags]

    newsub=[]
    i=0
    while i < len(subtitles):
        newsub.append(subtitles[i])
        i+=2

    return newsub


#author
def get_author(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    word="dd"

    tags = soup.find_all(word, attrs={"class":"autor"})
    authors=[c.getText().replace(">", "").strip() for c in tags]
    newaut=[]
    i=0
    while i < len(authors):
        newaut.append(authors[i])
        i+=2
    return newaut

#images
def get_image_list(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    pics = soup.find_all("img")
    image_list=[]
    for i in range(1,len(pics)-7):
        image_list.append(pics[i].get("src"))    
    return image_list