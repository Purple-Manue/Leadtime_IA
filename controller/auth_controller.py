from streamlit_authenticator import Authenticate

# Fonction d'authentification
def authenticate_user():
    lesDonneesDesComptes = {
        'usernames': {
            'utilisateur': {
                'name': 'utilisateur',
                'password': 'utilisateurMDP',
                'email': 'utilisateur@gmail.com',
                'failed_login_attemps': 0,
                'logged_in': False,
                'role': 'utilisateur'
            },
            'root': {
                'name': 'root',
                'password': 'rootMDP',
                'email': 'admin@gmail.com',
                'failed_login_attemps': 0,
                'logged_in': False,
                'role': 'administrateur'
            }
        }
    }

    # Initialiser l'authentification :
    authenticator = Authenticate(
        lesDonneesDesComptes,  # Les données des comptes
        "cookie name",  # Le nom du cookie
        "cookie key",  # La clé du cookie
        30  # Le nombre de jours avant que le cookie expire
    )

    authenticator.login()  # Tentative de connexion

    return authenticator