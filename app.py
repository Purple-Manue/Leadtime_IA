import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from PIL import Image
from view.display import display_main_page
from controller.project_controller import handle_user_input
from model.data_handler import load_data

# Titre et description de l'application
st.set_page_config(page_title="Leadtime IA", page_icon=":guardsman:", layout="centered")
st.title("Leadtime IA")
st.subheader("Une solution d'IA pour optimiser la gestion des stocks et des approvisionnements.")

# Afficher la page principale
display_main_page()

# Appeler la logique du contrôleur
handle_user_input()

# Exemple de chargement des données en back-end (cela pourrait être déclenché par une action de l'utilisateur)
if st.button("Charger les données"):
    file_path = 'data/ligne commande en cours.xlsx'  # À adapter selon le fichier d'entrée
    data_preview = load_data(file_path)
    st.write("Aperçu des données :", data_preview)

