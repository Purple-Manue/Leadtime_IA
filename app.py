import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from controller.auth_controller import authenticate_user
from view.display import display_main_page
from view.navbar import display_navbar
from model.data_handler import load_data
from model.data_processing import process_data
from plotting.plotting import create_graphs

# Ajouter le contenu de l'application ici
st.title("Leadtime IA")
st.subheader("Une solution d'IA pour optimiser la gestion des stocks et des approvisionnements.")

# Authentification
authenticator = authenticate_user()

# Ajouter le menu de navigation
selection = display_navbar()

# Vérifier si l'utilisateur est authentifié :
if st.session_state["authentication_status"]:
    # Afficher la page principale après authentification
    display_main_page()

    # Afficher le contenu en fonction de la sélection
    if selection == "Accueil":
        st.write("Bienvenue sur la page d'accueil de Leadtime IA!")
    
    elif selection == "Commandes":
        st.write("Gérer les commandes ici")
        # Afficher des informations supplémentaires sur les commandes si nécessaire

    elif selection == "Rapports":
        st.write("Afficher les rapports d'analyse et de performance")
        
        # Charger et afficher les données en fonction des interactions
        if "commande_df" not in st.session_state:
            st.session_state["commande_df"] = None
            st.session_state["livraison_df"] = None

        if st.button("Charger les données"):
            file_path = 'data/ligne commande en cours.xlsx'  # À adapter selon le fichier d'entrée
            try:
                # Charger les données
                data_preview = load_data(file_path)
                st.write("Aperçu des données :", data_preview)

                # Charger les fichiers Excel
                commande_df = pd.read_excel('data/ligne commande en cours.xlsx')
                livraison_df = pd.read_excel('data/livraison commande fournisseur.xlsx')
                
                # Sauvegarder les données dans la session pour éviter de recharger les fichiers à chaque clic
                st.session_state["commande_df"] = commande_df
                st.session_state["livraison_df"] = livraison_df
            except Exception as e:
                st.error(f"Erreur lors du chargement des données : {e}")
                st.stop()  # Arrêter l'exécution si une erreur se produit

        if st.session_state["commande_df"] is not None and st.session_state["livraison_df"] is not None:
            commande_df = st.session_state["commande_df"]
            livraison_df = st.session_state["livraison_df"]

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

            # Créer un graphique interactif avec Plotly
            fig = px.bar(filtered_data, x='PURCHID', y='QTYORDERED', title=f"Ventes pour {client_select}")
            st.plotly_chart(fig)

            # Créer une heatmap de corrélation avec Seaborn
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
    st.warning('Les champs username et mot de passe doivent être remplis')
