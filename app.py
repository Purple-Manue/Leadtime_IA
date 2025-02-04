import streamlit as st
import pandas as pd
from datetime import date  # Importation correcte de 'date'
from datetime import time  # Importation pour l'heure

# Exemple de code Streamlit avec date_input
st.date_input("Sélectionnez votre date de naissance", max_value=date.today())


st.date_input("Sélectionnez votre date de naissance")

st.time_input("Configurez une alarme à ", time(7, 30))


st.write("Hello World")

st.title("Le titre de ma page")
st.header("Une En-tête Importante")
st.subheader("Une En-tête Secondaire")
st.text("Mon texte classique")
st.markdown(''' :rainbow: :rainbow[Mon markdown] ''')
st.write(
    pd.DataFrame({
            "Cartes": ['Nom 1', 'Nom 2', 'Nom 3', 'Nom 4'],
            "Quantité": [0, 1, 0, 3]}
    )
)
if st.button("Ajouter"):
    st.write("+1")
    
st.checkbox('Tu es incollable sur l\'univers du Roi ion.')
st.write('___')
st.radio("Est-ce que Le Roi lion est le meilleur Disney ?",
['Oui !', 'Evidemment !', 'La question ne se pose même pas.'])
st.write('___')
st.toggle("Tu as vu Le Roi lion", value=True)
st.write('___')
st.selectbox("Qui a tué Mufasa ?",
['Simba', 'Scar', 'Zazu'])
st.write('___')
st.multiselect("Quels sont vos personnages favoris ?",
['Simba', 'Mufasa', 'Scar', 'Nala'])
st.write('___')
st.select_slider("Donnez votre appréciation sur le Roi lion",
['Mauvais', 'Bon', 'Excellent'], value='Excellent')

st.text_input("Quel est le titre de votre film favori ?", "Le Roi lion :D")

st.text_area("Peux-tu expliquer pourquoi c'est ton film favoris")

st.number_input("Tu en possèdes :", min_value=0)
st.slider("Sélectionnez la plage de date :",
           min_value=1923,
           max_value=date.today().year,
           value=(1923, date.today().year)
          )
st.date_input("Sélectionnez votre date de naissance")

st.time_input("Configurez une alarme à ", time(7, 30))