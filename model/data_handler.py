import pandas as pd

# Fonction pour charger les données en back-end
def load_data(file_path):
    """Chargement et traitement sécurisé des données"""
    try:
        df = pd.read_excel(file_path)  # Charger le fichier Excel
        # On peut ajouter ici des traitements comme le nettoyage des données
        return df.head()  # Retourne un aperçu des données
    except Exception as e:
        return f"Erreur lors du chargement des données : {str(e)}"
