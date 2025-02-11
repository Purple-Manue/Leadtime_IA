import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from streamlit_authenticator import Authenticate
#from controller.auth_controller import authenticate_user  # Importer la fonction d'authentification
from view.display import display_main_page  # Importer la fonction pour afficher la page principale
from model.data_handler import load_data  # Importer la fonction pour charger les données
from model.data_processing import process_data  # Importer la fonction pour traiter les données
from plotting.plotting import create_graphs  # Importer la fonction pour générer des graphiques

# Ajouter le contenu de l'application ici
st.title("Leadtime IA")
st.subheader("Une solution d'IA pour optimiser la gestion des stocks et des approvisionnements.")

# Nos données utilisateurs doivent respecter ce format
lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

authenticator.login()


if st.session_state["authentication_status"]:
  # Afficher la page principale après authentification
  display_main_page()

  # Exemple de chargement des données en back-end
  if st.button("Charger les données"):
    file_path = 'data/ligne commande en cours.xlsx'  # À adapter selon le fichier d'entrée
    try:
        # Charger les données
        data_preview = load_data(file_path)
        st.write("Aperçu des données :", data_preview)
    except Exception as e:
        st.error(f"Erreur lors du chargement des données : {e}")

    # Charger les fichiers Excel
    try:
        commande_df = pd.read_excel('data/ligne commande en cours.xlsx')
        livraison_df = pd.read_excel('data/livraison commande fournisseur.xlsx')
    except Exception as e:
        st.error(f"Erreur lors du chargement des fichiers Excel : {e}")
        st.stop()  # Arrêter l'exécution si une erreur se produit

    # Nettoyer les espaces dans les noms de colonnes
    commande_df.columns = commande_df.columns.str.strip()

    # Afficher les premières lignes des données
    st.write("Aperçu des données Commandes :")
    st.write(commande_df.head())
    st.write("Aperçu des données Livraisons :")
    st.write(livraison_df.head())

    # Filtrer les données par fournisseur (ici, la colonne est 'VENDACCOUNT')
    client_select = st.selectbox('Sélectionner un fournisseur', commande_df['VENDACCOUNT'].unique())

    # Filtrer les données en fonction du fournisseur sélectionné
    filtered_data = commande_df[commande_df['VENDACCOUNT'] == client_select]
    st.write(filtered_data)

    # Créer un graphique interactif avec Plotly (modification selon les colonnes 'PURCHID' et 'QTYORDERED')
    fig = px.bar(filtered_data, x='PURCHID', y='QTYORDERED', title=f"Ventes pour {client_select}")
    st.plotly_chart(fig)

    # Créer une heatmap de corrélation avec Seaborn (fonctionne sur les colonnes numériques uniquement)
    numeric_cols = commande_df.select_dtypes(include=['float64', 'int64']).columns
    corr = commande_df[numeric_cols].corr()

    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    ax.set_title("Matrice de corrélation")
    st.pyplot(fig)

    # Alertes sur les retards de livraison
    retard_df = livraison_df[livraison_df['DATEPHYSICAL'] > livraison_df['DATEEXPECTED']]
    if not retard_df.empty:
        st.warning(f"Attention, il y a des retards dans les livraisons : {len(retard_df)} retards détectés.")

    # Afficher d'autres graphiques en utilisant les données traitées
    processed_data = process_data(commande_df)
    fig1, fig2, fig3 = create_graphs(processed_data)

    # Afficher les graphiques
    st.pyplot(fig1)
    st.pyplot(fig2)
    st.plotly_chart(fig3)

  # Le bouton de déconnexion
  authenticator.logout("Déconnexion")

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')

