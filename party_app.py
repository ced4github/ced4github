# -*- coding: utf-8 -*-
# Name - party_app.py
# Author : Cedric MALLET - cedric_mallet@hotmail.com
# Date created 11/11/2021
# Date updated 13/11/2021
# Description : WEB Application with streamlit

import streamlit as st
import pandas as pd
import os
import time

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

st.sidebar.title('Le passage à 2022')
jour = st.sidebar.selectbox(
    "Menu",
    ("Le lieu","Soirée du 31 Décembre", "Le 1er Janvier","Le coût","Le couchage")
)

if jour == "Le lieu":
    st.title('La villa "SmartLodge" de Chennevière sur Marne...')
    st.image('https://res.cloudinary.com/amenitiz/image/upload/w_500,dpr_auto,f_auto,q_auto:good/v1596118608/gnslsz8zmjo4fnpnhjnt.jpg', caption='La maison du bonheur pendant 2 jours')

    st.subheader('...la découverte du lieu...')
    st.markdown("""

        12 chambres à partager !    
        * 2 au rez-de-chaussée
        * 6 au premier étage
        * 4 au troisième étage

        on va devoir faire du groupir ....

        *(le détail ci-dessous, vous pouvez faire du scrolling intégré)*
    """)
    st.components.v1.iframe('https://www.smartlodge-chennevieres.fr/fr/page/la-propriete', height=900, scrolling=True)

if jour == "Soirée du 31 Décembre":
    st.title('The party will start @6pm !')
    st.subheader('En apéritif...')
    st.markdown("""

        Stand-up apéro dancing sur lit de petits fours accompagnés de ses cocktails maison et champagne pour les intimes
        - Bon *l'alcool sera gérée par nous-même* et on divisera ensuite 
        

    """)
    st.image('https://cdn.shopify.com/s/files/1/1344/6283/products/NA250L_2000x.jpg?v=1548028588', caption='consommer avec modération...')
    st.subheader('au coeur du sujet...')
    st.markdown("""

        Plats du terroir accompagnés de ses vins nationaux ! 
        - La encore *l'alcool est en gestion interne*   
    """)

    st.image('https://www.parisinfo.com/var/otcp/sites/images/media/1.-photos/04.-restauration-630-x-405/menu-sp%C3%A9cialit%C3%A9s-fran%C3%A7aises-%7C-630x405-%7C-%C2%A9-thinkstock/10216908-1-fre-FR/Menu-sp%C3%A9cialit%C3%A9s-fran%C3%A7aises-%7C-630x405-%7C-%C2%A9-Thinkstock.jpg')

    st.subheader('pour faire rou...couler...')
    st.markdown("""

        Le frometon accompagné aussi de ses vins nationaux !    

        et des migniardises pour les gamines ....

    """)

    st.image('https://blackrivercheese.com/wp-content/uploads/2020/03/BRC_Recipes_Header_DessertBoard.jpg', caption='ok ca ressemblera pas a ca mais vous avez compris l\'idée')

    st.subheader('...et place à la disco Boris...')
    st.markdown("""

        Ca sera chaud !    

        ....dans les T-shirts et les maillots :confetti_ball:

    """)

    st.image('https://cdn.deguisetoi.fr/media/blog_left_content/fra/5d1f2189b8537_soiree-a-theme-entre-amis-mode-d-emploi.jpg', caption='un peu cliché')
    col1, col2 = st.columns(2)
    with col1:
        st.image('https://c.tenor.com/DKVCnKDquKAAAAAM/old-dance-elderly.gif', caption='...peut-être plus comme ca')
    with col2:
        st.image('https://c.tenor.com/arL_1cVEX5UAAAAM/dancing-flossing.gif', caption='...ou ca')

if jour == "Le 1er Janvier":
    st.title('Dur la récup du lendemain...')
    st.image('https://parismatch.be/app/uploads/2018/02/hangover.jpg', caption='Putain... 2 jours')
    st.subheader('...et pour ceux qui auront survécu...')
    st.markdown("""

        Petite promenade en bord de Marne et restauration allégée !    
    """)
    st.image('https://static1.terrafemina.com/articles/6/35/18/86/@/524149-11-remedes-anti-gueule-de-bois-qui-march-953x0-2.jpeg', caption='ca va le faire')
    st.markdown("""

        enfin presque ....

    """)
    st.image('https://cdn.vox-cdn.com/thumbor/LDguMoaLglKzWfDoScChJPJ6F5w=/0x0:8256x5504/2570x1446/filters:focal(3456x1020:4776x2340):format(webp)/cdn.vox-cdn.com/uploads/chorus_image/image/70017525/1235975361.0.jpg', caption='...une thématique en vue ?')

if jour == "Le coût":
    st.title('Les frais sont désormais séparés entre le coût logement (fixés) et le coût de la bouffe qui varie encore en fonction des choix !')
    #construire le dataframe
    dflogement = pd.DataFrame({
        'index': ['Dada','Rage','Nours','Funes','Nico','Math','Nonos','Lolo','Dom','Ced'],
        '31 Decembre': [374,345,230,431,316,230,201,374,316,230],
        '1er Janvier': [376,0,188,0,259,188,165,0,235,329],
        }).set_index('index')

    dfbouffe = pd.DataFrame({
        'index': ['Dada','Rage','Nours','Funes','Nico','Math','Nonos','Lolo','Dom','Ced'],
        '31 Decembre': [180,150,120,195,165,120,105,180,165,120],
        '1er Janvier': [160,0,80,0,110,80,70,0,100,140],
        }).set_index('index')

    st.subheader("Lodging cost - based on confirmed attendees")
    st.bar_chart(dflogement)
    st.subheader("Food cost - simulation with 60 euros on 31 st for adult and 40 euros on 1er for adult")
    st.bar_chart(dfbouffe)
    with st.expander("Voir le détail des coûts"):
        st.info("""
        Le tableau reprend la cotisation a la teuf de l'année 2021...
        ... et on va dire aussi 2022 (étant donné que cela se termine le 2 Janvier)
        """)
        st.warning("""
        - 31 décembre: Ceci correspond à 115EUR (adulte full price), ado .75 and kid .5
        - 1er janvier: Ceci correspond à 94EUR (adulte full price), ado .75 and kid .5
        """)
        st.table(dflogement.style.set_table_styles(styles).set_caption("Image by Cedric le magnifi..."))
        st.info("""
        - 31 décembre: Ceci correspond à 60EUR (adulte full price), ado .75 and kid .5
        - 1er janvier: Ceci correspond à 40EUR (adulte full price), ado .75 and kid .5
        """)
        st.table(dfbouffe.style.set_table_styles(styles).set_caption("Image by Cedric le magnifi..."))
if jour == "Le couchage":
    st.title('Les lits sont désormais répartis avec des chambres enfants/ados et les chambres adultes - Pour ceux qui se levent le 1er - pas de Rez-de chaussée)!')
    st.warning("""
        Il faut des matelas supplémentaires comme suivant:
        - matelas 2 places: Nonos amène
        - matelas 1 places: Math amène
        - matelas 1 places: Rage amène
        - matelas 1 places: Nours amène
        - matelas 1 places: Dada amène
        """)
    dfcouchage = pd.DataFrame({
        'index': ['Adultes','Ados girls','Ados boys','Kids girls','Kids boys'],
        'Nb personnes': [19,3,3,3,3],
        'Nb chambres': [9,1,1,1,1],
        }).set_index('index')
    with st.expander("Voir la répartition des chambres en nombre et allocation temporaire"):
        st.table(dfcouchage.style.set_table_styles(styles).set_caption("Image by Ced..."))
        st.warning("""
        ***Rez-de-chaussée***
        - Les kids Boys vont avoir la chambre 2 avec 1 matelas simple à ajouter
        - Math gang: chambre 1
        - Salon 2 canapés pour 2 gardiens qui devront monter la garde
        - Les 3 Ados boys squattent le bureau ou le palier du 2eme niveau avec 1 matelas double et 1 matelas simple

        ***1er étage***
        - 6 chambres adultes
            - chb3: Dom/Alex VM
            - chb4: Dada/Alex DB
            - chb5: Ced/Mutsu
            - chb6: Nico/Ninie
            - chb7: Funes/Ivy
            - chb8: Nours/Celine

        ***2éme étage***
        - 2 chambres adultes
            - chb9: Rage/Caro
            - chb10: Lolo/Virginie
        - Les Ados Girls chb11 avec 1 matelas simple à ajouter
        - Les 3 Kids Girls chb12 avec 1 matelas simple à ajouter
        """)

    st.markdown('<a href="mailto:cedric_mallet@hotmail.com">Pour obtenir davantage d\'information, merci de contacter Ced</a>', unsafe_allow_html=True)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)