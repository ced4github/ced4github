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

st.set_page_config(
     page_title="Welcome to Ced",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'Email: cedric_mallet@hotmail.com',
         'About': "# This is an *extremely* cool app!"
     }
)

st.sidebar.title('Party events')
jour = st.sidebar.selectbox(
    "So much to catch-up - Choose the day",
    ("31 Decembre", "1er Janvier")
)
Dada = st.checkbox('Dada')
Rage = st.checkbox('Rage')
Nours = st.checkbox('Nours')
Funes = st.checkbox('Funes')
Nico = st.checkbox('Nico')
Math = st.checkbox('Math')
Nonos = st.checkbox('Nonos')
Lolo = st.checkbox('Lolo')
Dom = st.checkbox('Dom')
Ced = st.checkbox('Ced')

if jour == "31 Decembre":
    st.write('The party will start !')
    image = Image.open('https://www.abritel.fr/location-vacances/p1922594')
    st.image(image, caption='La maison du bonheur pendant 2 jours')
    st.ballons()

if jour == "1er Janvier":
    st.write('La recup...')
    image = Image.open('https://parismatch.be/app/uploads/2018/02/hangover.jpg')
    st.image(image, caption='Putain... 2 jours')


# Hiding the right menu
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)
