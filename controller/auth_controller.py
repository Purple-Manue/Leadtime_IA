import streamlit as st
from streamlit_authenticator import Authenticate

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
   'role': 'administrateur'}
  }
                        }
authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

# Fonction d'authentification
def authenticate_user():  
    authenticator = Authenticate(  
        # Vos paramètres d'authentification ici  
        usernames=lesDonneesDesComptes['usernames'],  
        # Autres paramètres nécessaires  
    )  
    
    authentication_status = authenticator.login("Nom d'utilisateur", "Mot de passe")  
    
    if authentication_status:  
        return True, authenticator  
    else:  
        return False, None
    
authenticator.login()
print("Fonction authenticate_user appelée")