# data_processing.py
import pandas as pd
import plotly.express as px

def process_data(df):
    # Exemple de traitement des données : convertit les dates et nettoie les données
    df['DELIVERYDATE'] = pd.to_datetime(df['DELIVERYDATE'], errors='coerce')
    #df['DATEPHYSICAL'] = pd.to_datetime(df['DATEPHYSICAL'], errors='coerce')


    return df
