import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def create_graphs(df):
    # Convertir 'NAME' en str si ce n'est pas déjà le cas
    df['NAME'] = df['NAME'].astype(str)
    
    # Graphique des quantités commandées par client
    fig1, ax1 = plt.subplots()
    ax1.bar(df['NAME'], df['QTYORDERED'])
    ax1.set_xlabel('Nom du Client')
    ax1.set_ylabel('Quantité Commandée')
    ax1.set_title('Quantité Commandée par Client')

    # Graphique des quantités commandées par date de livraison
    fig2, ax2 = plt.subplots()
    ax2.plot(df['DELIVERYDATE'], df['QTYORDERED'])
    ax2.set_xlabel('Date de Livraison')
    ax2.set_ylabel('Quantité Commandée')
    ax2.set_title('Quantité Commandée par Date de Livraison')

    # Remplacer les NaN par 0 avant de calculer la corrélation
    df = df.fillna(0)

    # Sélectionner uniquement les colonnes numériques avant de calculer la corrélation
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    corr_df = df[numeric_cols]

    # Calculer la matrice de corrélation
    corr = corr_df.corr()

    # Graphique de la matrice de corrélation
    fig3, ax3 = plt.subplots()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax3)
    ax3.set_title('Matrice de Corrélation')

    return fig1, fig2, fig3  # Retourner les trois graphiques

