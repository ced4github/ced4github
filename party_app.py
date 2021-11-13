# -*- coding: utf-8 -*-
# Name - party_app.py
# Author : Cedric MALLET - cedric_mallet@hotmail.com
# Date created 11/11/2021
# Date updated 11/11/2021
# Description : WEB Application with streamlit

import streamlit as st
import pandas as pd
import os
from PIL import Image
import numpy as np


st.set_page_config(
     page_title="Welcome to Ced",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded")

styles = [
    dict(selector="tr:hover",
                props=[("background", "#f4f4f4")]),
    dict(selector="th", props=[("color", "#fff"),
                               ("border", "1px solid #eee"),
                               ("padding", "12px 35px"),
                               ("border-collapse", "collapse"),
                               ("background", "#00cccc"),
                               ("text-transform", "uppercase"),
                               ("font-size", "18px")
                               ]),
    dict(selector="td", props=[("color", "#999"),
                               ("border", "1px solid #eee"),
                               ("padding", "12px 35px"),
                               ("border-collapse", "collapse"),
                               ("font-size", "15px")
                               ]),
    dict(selector="table", props=[
                                    ("font-family" , 'Arial'),
                                    ("margin" , "25px auto"),
                                    ("border-collapse" , "collapse"),
                                    ("border" , "1px solid #eee"),
                                    ("border-bottom" , "2px solid #00cccc"),                                    
                                      ]),
    dict(selector="caption", props=[("caption-side", "bottom")])
]

st.sidebar.title('Party events description')
jour = st.sidebar.selectbox(
    "So much to catch-up",
    ("31 Decembre", "1er Janvier","cout")
)

if jour == "31 Decembre":
    st.title('The party will start !')
#    image = Image.open('https://www.abritel.fr/location-vacances/p1922594')
    st.image('https://res.cloudinary.com/amenitiz/image/upload/w_500,dpr_auto,f_auto,q_auto:good/v1596118608/gnslsz8zmjo4fnpnhjnt.jpg', caption='La maison du bonheur pendant 2 jours')
#    st.balloons()

if jour == "1er Janvier":
    st.title('Dur la recup du lendemain...')
#    image = Image.open('https://parismatch.be/app/uploads/2018/02/hangover.jpg')
    st.image('https://parismatch.be/app/uploads/2018/02/hangover.jpg', caption='Putain... 2 jours')

if jour == "cout":
    st.title('Les frais sont partagés et un premium est appliqué le soir du réveillon via un algorithme intelligent... comme moi !')
    #construire le dataframe
    df = pd.DataFrame({
        'index': ['Dada','Rage','Nours','Funes','Nico','Math','Nonos','Lolo','Dom','Ced'],
        '31 Decembre': [563,638,356,638,489,178,312,624,489,489],
        '1er Janvier': [360,0,180,0,248,90,158,0,225,315],
        }).set_index('index')

#    chart_data = pd.DataFrame(
#    np.array(['Dada','Rage','Nours','Funes','Nico','Math','Nonos','Lolo','Dom','Ced'],[563.5,637.5,356,637.5,489.5,178,311.5,623,489.5,489.5],[360,0,180,0,247.5,90,157.5,0,225,315]),
#    columns=["clan", "31 Decembre", "1er Janvier"])
#    st.bar_chart(chart_data)
    st.bar_chart(df)
    with st.expander("Voir le detail en tableau"):
        st.info("""
        Le tableau reprend la cotisation a la teuf de l'année 2021...
        ... et on va dire aussi 2022
        """)
        st.table(df.style.set_table_styles(styles).set_caption("Image by Author (Made by Cedric)"))

#        st.table(df.style.set_properties(**{'background-color': 'grey',
#        'color': 'black',
#        'border-color': 'blue'}))



# Hiding the right menu
#st.markdown(""" <style>
##MainMenu {visibility: hidden;}
#footer {visibility: hidden;}
#</style> """, unsafe_allow_html=True)
