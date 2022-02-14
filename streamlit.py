import streamlit as st
import pathlib as Path
import pandas as pd
import numpy as np
import plotly_express as px

cols = ['Customer ID','Date update order status','Sous-commande id', 'Commande Id', 'Total products with tax', 'Total paid with tax',\
        'Shipping Country name', 'Product name (include combination name)', 'Catégorie', 'Sous-Catégorie']
        
# 'Total voucher with tax', 

#@st.cache(persist=True)

data = pd.read_excel('data_yogah.xlsx', sheet_name='Exporter',parse_dates=['Date update order status'], usecols=cols)
data["jour"] = data['Date update order status'].dt.strftime('%Y-%m-%d')
data["mois_annee"] = data['Date update order status'].dt.strftime('%Y-%m')
data["annee"] = data['Date update order status'].dt.strftime('%Y')

st.title("Affichage des données !!!") 

st.write(data)

df = data.rename(columns={'Date update order status':'date_commande','Sous-commande id':'ss_cde_id','Commande Id':'cde_id',\
                          'Total products with tax':'total_prod','Total paid with tax':'total_paid','Shipping Country name':'pays_exped',\
                         'Product name (include combination name)':'produit','Catégorie':'categorie','Sous-Catégorie':'cous_categorie'})
# Nous allons remplacer la modalité "alimentaire" par "Alimentaire"
df['categorie']= df['categorie'].replace(['alimentaire'],['Alimentaire'])
tt = df.drop_duplicates(subset='cde_id')
#
#	st.title("Evolution du CA par mois")
#	fig2 = px.line(df_ca, x='mois_annee', y='total_paid')
#	ts_chart = st.plotly_chart(fig2)

st.title("Evolution du nombre de commande par mois")
an = st.radio("Selectionner une année : ",(2018,2019,2020,2021,2022))
if (an == 2018):
    df_18 = tt[tt["annee"]=='2018']
    df_ca = df_18.groupby("mois_annee").agg({"cde_id":np.size})
    df_ca.reset_index(inplace=True)
    fig1 = px.line(df_ca, x='mois_annee', y='cde_id')
    ts_chart = st.plotly_chart(fig1)
    
elif (an == 2019):
    df_19 = tt[tt["annee"]=='2019']
    df_ca = df_19.groupby("mois_annee").agg({"cde_id":np.size})
    df_ca.reset_index(inplace=True)
    fig1 = px.line(df_ca, x='mois_annee', y='cde_id')
    ts_chart = st.plotly_chart(fig1)

elif (an == 2020):
    df_20 = tt[tt["annee"]=='2020']
    df_ca = df_20.groupby("mois_annee").agg({"cde_id":np.size})
    df_ca.reset_index(inplace=True)
    fig1 = px.line(df_ca, x='mois_annee', y='cde_id')
    ts_chart = st.plotly_chart(fig1)
    
elif (an == 2021):
    df_21 = tt[tt["annee"]=='2021']
    df_ca = df_21.groupby("mois_annee").agg({"cde_id":np.size})
    df_ca.reset_index(inplace=True)
    fig1 = px.line(df_ca, x='mois_annee', y='cde_id')
    ts_chart = st.plotly_chart(fig1)
    
elif (an == 2022):
    df_22 = tt[tt["annee"]=='2022']
    df_ca = df_22.groupby("mois_annee").agg({"cde_id":np.size})
    df_ca.reset_index(inplace=True)
    fig1 = px.line(df_ca, x='mois_annee', y='cde_id')
    ts_chart = st.plotly_chart(fig1)
    
#st.markdown("<span style='font-size:18px'> Nombre Total de produit achetés : </span>",df.shape[0])
#st.write("Nombre Total de produit achetés : ",df.shape[0])
#st.write("Date de la première commande: 14 Juin 2018")


################################ CALCUL DU TAUX DE REACHAT PAR CATEGORIE DE PRODUIT ET PAR ANNÉE ###
# filtrer les catégro
