import os
import time
import sys

# Styles et Couleurs GRAS
BOLD = "\033[1m"
G = "\033[1;32m" # Vert Gras
R = "\033[1;31m" # Rouge Gras
Y = "\033[1;33m" # Jaune Gras
W = "\033[1;37m" # Blanc Gras
C = "\033[1;36m" # Cyan Gras

def update_system():
    os.system('clear')
    print(f"{BOLD}{C}╔═══════════════════════════════════════════╗")
    print(f"║        MISE À JOUR DU SYSTÈME SMM         ║")
    print(f"╚═══════════════════════════════════════════╝{W}")
    
    # Chemin vers le dossier local
    path = os.path.join(os.path.expanduser("~"), "insta-manager-pro")
    
    print(f"\n{BOLD}{Y}[*] Connexion au dépôt GitHub...{W}")
    time.sleep(1)
    
    try:
        # On s'assure d'être dans le bon dossier
        if os.path.exists(path):
            print(f"{BOLD}{Y}[*] Synchronisation des fichiers...{W}")
            # On force la mise à jour pour éviter les erreurs
            os.system(f'cd {path} && git reset --hard && git pull')
        else:
            print(f"{BOLD}{Y}[*] Réinstallation du dépôt...{W}")
            os.system(f'cd $HOME && git clone https://github.com/elinoj89-dotcom/insta-manager-pro.git')
        
        print(f"\n{BOLD}{G}[✔] MISE À JOUR RÉUSSIE !{W}")
        print(f"{BOLD}{Y}[*] Lancement du moteur...{W}")
        time.sleep(2)
        
        # TRÈS IMPORTANT : Lance le main.py du BOT (mot de passe)
        os.system(f'python {path}/main.py')
        
    except Exception as e:
        print(f"\n{BOLD}{R}[✘] Erreur lors de la mise à jour : {e}{W}")
        sys.exit()

if __name__ == "__main__":
    try:
        update_system()
    except KeyboardInterrupt:
        sys.exit()
        
