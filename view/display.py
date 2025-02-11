import streamlit as st
from PIL import Image
#from controller.auth_controller import authenticate_user  # Importer la fonction d'authentification

def display_main_page():
    """Affichage de la page d'accueil du projet"""
    # Afficher le logo
    try:
        image = Image.open("Img/Logo_LeadtimeIA.webp")
        st.image(image, caption="Logo Projet Leadtime IA", use_container_width=True)

        
    except FileNotFoundError:
        st.write("Logo non trouvé.")
    
    # Description du projet
    st.markdown("""**Leadtime IA** est un projet visant à améliorer la gestion des achats, de la logistique et des approvisionnements. Ce projet repose sur l'automatisation et l'optimisation des processus métiers à l'aide de l'intelligence artificielle.""")
    
    '''
    # Inputs utilisateur pour simuler la gestion du projet
    st.text_input("Quel est le titre de votre projet ?", "Mon Projet IA")
    st.text_area("Décrivez brièvement votre projet", "Entrez la description ici...")
    st.selectbox("Choisissez un modèle d'IA", ["Modèle A", "Modèle B", "Modèle C"])
    st.slider("Sélectionnez un niveau d'importance", 1, 10, 5)
    '''


    # Affichage d'un footer
    st.markdown("---")


    st.write("© 2025 - Projet Leadtime IA")