import os
import time

# Couleurs Style Screenshot
P = "\033[35m" # Violet
G = "\033[32m" # Vert
Y = "\033[33m" # Jaune
W = "\033[0m"  # Blanc

def install_menu():
    os.system('clear')
    print(f"{P}┌───────────────────────────────────────────┐")
    print(f"│            INSTALLATION SYSTEM            │")
    print(f"└───────────────────────────────────────────┘{W}")
    print(f"{G}(✓) Développeur = ELINO")
    print(f"(✓) Tool Name   = SMM PRO{W}")
    print("-" * 45)
    print(f"{W}[1] TOUT INSTALLER (PKG & BOT)")
    print(f"[0] QUITTER")
    
    choice = input(f"\n{P}[?] Votre Choix : {W}")
    
    if choice == "1":
        print(f"\n{G}[*] 1/3 Mise à jour des paquets système...{W}")
        os.system('pkg update && pkg upgrade -y')
        
        print(f"\n{G}[*] 2/3 Installation des dépendances Python...{W}")
        # Installation des bibliothèques nécessaires pour ton bot
        os.system('pip install requests rich brotli zstandard --quiet')
        
        print(f"\n{G}[*] 3/3 Clonage du moteur principal...{W}")
        # Ton nouveau lien GitHub
        os.system('cd $HOME && git clone https://github.com/elinoj89-dotcom/insta-manager-pro.git')
        
        print(f"\n{Y}[!] Installation terminée avec succès !{W}")
        time.sleep(2)
        
        # On lance le verrou de sécurité (main.py) qui est dans le dossier INSTALL
        print(f"{G}[▶] Lancement du système de vérification...{W}")
        os.system('python main.py')
    else:
        print(f"{R}Fermeture du programme.{W}")
        exit()

if __name__ == "__main__":
    try:
        install_menu()
    except KeyboardInterrupt:
        exit()
        
