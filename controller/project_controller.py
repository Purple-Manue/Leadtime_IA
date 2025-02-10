import streamlit as st

def handle_user_input():
    """Gérer les actions de l'utilisateur, comme les clics sur les boutons"""
    # Par exemple, si un utilisateur clique sur un bouton de soumission
    if st.button("Soumettre"):
        title = st.text_input("Quel est le titre de votre projet ?")
        description = st.text_area("Décrivez brièvement votre projet")
        model = st.selectbox("Choisissez un modèle d'IA", ["Modèle A", "Modèle B", "Modèle C"])
        importance = st.slider("Sélectionnez un niveau d'importance", 1, 10, 5)
        
        # Afficher un message de confirmation (ou stocker les données)
        st.write(f"Votre projet '{title}' a été soumis avec le modèle '{model}' et un niveau d'importance de {importance}.")
