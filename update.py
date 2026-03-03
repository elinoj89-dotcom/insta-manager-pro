import os
import time
import sys

# Couleurs pour le style
G = "\033[32m" # Vert
R = "\033[31m" # Rouge
Y = "\033[33m" # Jaune
W = "\033[0m"  # Blanc
C = "\033[36m" # Cyan

def update_system():
    os.system('clear')
    print(f"{C}╔═══════════════════════════════════════════╗")
    print(f"║        MISE À JOUR DU SYSTÈME SMM         ║")
    print(f"╚═══════════════════════════════════════════╝{W}")
    
    # Chemin vers le dossier local
    path = os.path.join(os.path.expanduser("~"), "insta-manager-pro")
    
    print(f"\n{Y}[*] Connexion au dépôt GitHub...{W}")
    time.sleep(1)
    
    try:
        # On s'assure d'être dans le bon dossier
        if os.path.exists(path):
            # git reset --hard efface les modifs locales pour éviter les conflits
            print(f"{Y}[*] Synchronisation des fichiers...{W}")
            os.system(f'cd {path} && git reset --hard && git pull https://github.com/elinoj89-dotcom/insta-manager-pro.git')
        else:
            # Si le dossier n'existe pas, on le clone proprement
            print(f"{Y}[*] Réinstallation du dépôt...{W}")
            os.system(f'cd $HOME && git clone https://github.com/elinoj89-dotcom/insta-manager-pro.git')
        
        print(f"\n{G}[✔] MISE À JOUR RÉUSSIE !{W}")
        print(f"{Y}[*] Redémarrage du système...{W}")
        time.sleep(2)
        
        # Relance le menu principal (main.py dans INSTALL)
        os.system('python ~/INSTALL/main.py')
        
    except Exception as e:
        print(f"\n{R}[✘] Erreur lors de la mise à jour : {e}{W}")
        print(f"{Y}[!] Vérifiez votre connexion internet.{W}")
        input(f"\n{C}[ Appuyez sur Entrée pour quitter ]{W}")
        sys.exit()

if __name__ == "__main__":
    try:
        update_system()
    except KeyboardInterrupt:
        print(f"\n{R}[!] Annulé.{W}")
        sys.exit()
            
