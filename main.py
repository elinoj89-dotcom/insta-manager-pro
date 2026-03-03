import os
import sys
import time

# Couleurs
G = "\033[32m" # Vert
R = "\033[31m" # Rouge
Y = "\033[33m" # Jaune
W = "\033[0m"  # Blanc

def launch_bot():
    os.system('clear')
    print(f"{Y}╔═══════════════════════════════════════════╗")
    print(f"║          DÉMARRAGE DU MOTEUR SMM          ║")
    print(f"╚═══════════════════════════════════════════╝{W}")
    
    # Vérification du mot de passe de secours
    pwd = input(f"\n{Y}(🔑) Mot De Passe de Sécurité : {W}")
    
    if pwd == "Elino21#2006":
        print(f"\n{G}[✔] Accès autorisé. Initialisation...{W}")
        time.sleep(1)
        
        # Vérifie si le dossier de ressources existe, sinon le clone
        # Note : J'ai adapté le nom du dossier pour qu'il corresponde au dépôt
        target_folder = os.path.join(os.path.expanduser("~"), "insta-manager-pro")
        
        if not os.path.exists(target_folder):
            print(f"{Y}[*] Téléchargement des ressources (insta-manager-pro)...{W}")
            os.system('cd $HOME && git clone https://github.com/elinoj89-dotcom/insta-manager-pro.git')
        
        # Lancement effectif du bot
        # Assure-toi que bot.py se trouve bien à la racine de ce dossier
        print(f"{G}[▶] Lancement de bot.py...{W}")
        os.system(f'cd {target_folder} && python bot.py')
    else:
        print(f"{R}[✘] Mot de passe incorrect. Fermeture.{W}")
        sys.exit()

if __name__ == "__main__":
    try:
        launch_bot()
    except KeyboardInterrupt:
        print(f"\n{R}[!] Interrompu par l'utilisateur.{W}")
        sys.exit()
        
