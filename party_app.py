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
    dico = {"clan": ['Dada','Rage','Nours','Funes','Nico','Math','Nonos','Lolo','Dom','Ced'],
        "31 Decembre":[563.5,637.5,356,637.5,489.5,178,311.5,623,489.5,489.5],
        "1er Janvier":[360,0,180,0,247.5,90,157.5,0,225,315],
        }
    df = pd.DataFrame(data=dico)
    st.dataframe(df)

    chart_data = pd.DataFrame(
    np.array(['Dada','Rage','Nours','Funes','Nico','Math','Nonos','Lolo','Dom','Ced'],[563.5,637.5,356,637.5,489.5,178,311.5,623,489.5,489.5],[360,0,180,0,247.5,90,157.5,0,225,315]),
    columns=["clan", "31 Decembre", "1er Janvier"])
    st.bar_chart(chart_data)
#    st.bar_chart(df)


# Hiding the right menu
#st.markdown(""" <style>
##MainMenu {visibility: hidden;}
#footer {visibility: hidden;}
#</style> """, unsafe_allow_html=True)
