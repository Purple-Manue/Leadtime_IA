import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from PIL import Image

# Titre de la page
st.set_page_config(page_title="Projet Fil Rouge IA", page_icon=":guardsman:", layout="centered")

# En-têtes
st.title("Leadtime IA")
st.subheader("Ce projet vise à concevoir et implémenter une solution d'intelligence artificielle (IA) pour améliorer la gestion des achats, de la logistique et des approvisionnements. Il repose sur la collecte des besoins des utilisateurs afin d'automatiser et d'optimiser les processus métiers.")

# Charger et afficher l'image avec PIL
image_path = "Img/Logo_LeadtimeIA.webp"

# Essayer de charger l'image et l'afficher
try:
    image = Image.open(image_path)
    st.image(image, caption="Logo Projet Fil Rouge", use_column_width=True)  # Affichage de l'image redimensionnée
except FileNotFoundError:
    st.write(f"Image non trouvée à l'emplacement : {image_path}")  # Fermeture correcte de la f-string



# Section de texte avec du markdown
st.markdown('''
    Voici une explication de mon projet de Fil Rouge IA : 
    Le but est de développer une solution d'intelligence artificielle pour améliorer la gestion des stocks et des approvisionnements.
    ''')

# Inputs utilisateur
st.text_input("Quel est le titre de votre projet ?", "Mon Projet IA")
st.text_area("Décrivez brièvement votre projet", "Entrez la description ici...")
st.selectbox("Choisissez un modèle d'IA", ["Modèle A", "Modèle B", "Modèle C"])
st.slider("Sélectionnez un niveau d'importance", 1, 10, 5)

# Bouton pour soumettre
if st.button("Soumettre"):
    st.write("Votre projet a été soumis !")

# Ajout d'un footer
st.markdown("---")
st.write("© 2025 - Projet Fil Rouge IA")
