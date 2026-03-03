import os
import time
import sys

# Couleurs pour le style PKG
G = "\033[32m" # Vert
R = "\033[31m" # Rouge
W = "\033[0m"  # Blanc
P = "\033[35m" # Violet
Y = "\033[33m" # Jaune

def clear():
    os.system('clear')

def check_security():
    clear()
    print(f"{P}┌───────────────────────────────────────────┐")
    print(f"│       SYSTÈME DE SÉCURITÉ ELINO v2.6      │")
    print(f"└───────────────────────────────────────────┘{W}")
    
    pwd = input(f"\n{Y}[?] Entrez le mot de passe d'accès : {W}")
    
    if pwd == "Elino21#2006":
        print(f"{G}[✔] Accès autorisé. Chargement du menu...{W}")
        time.sleep(1.5)
        main_menu()
    else:
        print(f"{R}[✘] Mot de passe incorrect. Fermeture.{W}")
        sys.exit()

def main_menu():
    clear()
    print(f"{P}┌───────────────────────────────────────────┐")
    print(f"│           PANNEAU DE CONTRÔLE SMM         │")
    print(f"└───────────────────────────────────────────┘{W}")
    print(f"{G}(✓) Github    = Lariot08")
    print(f"(✓) Statut    = Connecté{W}")
    print("-" * 45)
    print(f"{W}[1] {G}Installer & Lancer SMM BOT{W}")
    print(f"{W}[2] {G}Mise à jour Système{W}")
    print(f"{W}[0] {R}Quitter{W}")
    print("-" * 45)
    
    choice = input(f"{Y}[?] Choix : {W}")

    if choice == "1":
        print(f"\n{P}[*] Préparation de l'environnement...{W}")
        # Installation automatique de instabot au cas où
        os.system('pip install instabot --quiet')
        
        # Séquence de téléchargement demandée
        print(f"{G}[*] Téléchargement du module SMM...{W}")
        os.system('cd $HOME && git clone https://github.com/Lariot08/SMM')
        
        print(f"{G}[*] Lancement du bot...{W}")
        time.sleep(1)
        # On se déplace dans SMM et on lance bot.py
        os.system('cd $HOME/SMM && python bot.py')

    elif choice == "0":
        sys.exit()
    else:
        main_menu()

if __name__ == "__main__":
    check_security()
    
