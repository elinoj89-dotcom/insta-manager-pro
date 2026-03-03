import os
import time
import sys

# Styles et Couleurs GRAS
BOLD = "\033[1m"
G = "\033[1;32m" ; Y = "\033[1;33m" ; W = "\033[1;37m" ; C = "\033[1;36m"

def update_system():
    os.system('clear')
    print(f"{BOLD}{C}╔═══════════════════════════════════════════╗")
    print(f"║        MISE À JOUR DU SYSTÈME SMM         ║")
    print(f"╚═══════════════════════════════════════════╝{W}")
    
    path = os.path.join(os.path.expanduser("~"), "insta-manager-pro")
    
    print(f"\n{BOLD}{Y}[*] Connexion au dépôt GitHub...{W}")
    time.sleep(1)
    
    try:
        if os.path.exists(path):
            print(f"{BOLD}{Y}[*] Synchronisation des fichiers...{W}")
            os.system(f'cd {path} && git reset --hard && git pull')
        else:
            print(f"{BOLD}{Y}[*] Réinstallation du dépôt...{W}")
            os.system(f'cd $HOME && git clone https://github.com/elinoj89-dotcom/insta-manager-pro.git')
        
        print(f"\n{BOLD}{G}[✔] MISE À JOUR RÉUSSIE !{W}")
        print(f"{BOLD}{Y}[*] Lancement du moteur de sécurité...{W}")
        time.sleep(2)
        
        # Lance le fichier main.py qui demande le mot de passe Elino21#2006
        os.system(f'python {path}/main.py')
        
    except Exception as e:
        print(f"\n{BOLD}{R}[✘] Erreur : {e}{W}")
        sys.exit()

if __name__ == "__main__":
    update_system()
                     
