import os
import sys
import time

# Styles et Couleurs (Style GRAS activé)
BOLD = "\033[1m"
G = "\033[1;32m" # Vert Gras
R = "\033[1;31m" # Rouge Gras
Y = "\033[1;33m" # Jaune Gras
W = "\033[1;37m" # Blanc Gras
B = "\033[1;34m" # Bleu Gras
C = "\033[1;36m" # Cyan Gras

def launch_bot():
    os.system('clear')
    
    # En-tête de sécurité en Style Gras
    print(f"{BOLD}{Y}╔═══════════════════════════════════════════╗")
    print(f"║          DÉMARRAGE DU MOTEUR SMM          ║")
    print(f"╚═══════════════════════════════════════════╝{W}")
    
    # Demande du mot de passe avec curseur en Gras
    pwd = input(f"\n{BOLD}{Y}(🔑) Mot De Passe de Sécurité : {W}{BOLD}")
    
    if pwd == "Elino21#2006":
        print(f"\n{BOLD}{G}[✔] Accès autorisé. Initialisation...{W}")
        time.sleep(1)
        
        # Vérification du dossier cible
        target_folder = os.path.join(os.path.expanduser("~"), "insta-manager-pro")
        
        if not os.path.exists(target_folder):
            print(f"{BOLD}{Y}[*] Téléchargement des ressources (SMM PRO)...{W}")
            os.system('cd $HOME && git clone https://github.com/elinoj89-dotcom/insta-manager-pro.git')
        
        # Lancement effectif du bot en Gras
        print(f"{BOLD}{B}[▶] Lancement du moteur bot.py...{W}")
        os.system(f'cd {target_folder} && python bot.py')
    else:
        print(f"\n{BOLD}{R}[✘] Mot de passe incorrect. Fermeture.{W}")
        sys.exit()

if __name__ == "__main__":
    try:
        launch_bot()
    except KeyboardInterrupt:
        print(f"\n{BOLD}{R}[!] Interrompu par l'utilisateur.{W}")
        sys.exit()
        
