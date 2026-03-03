import os
import time
import sys
import instaloader

# Styles et Couleurs GRAS
BOLD = "\033[1m"
G = "\033[1;32m" ; Y = "\033[1;33m" ; W = "\033[1;37m" 
C = "\033[1;36m" ; B = "\033[1;34m" ; R = "\033[1;31m"

def extract_followers():
    os.system('clear')
    print(f"{BOLD}{C}╔═══════════════════════════════════════════╗")
    print(f"║         CONNEXION SÉCURISÉE INSTA         ║")
    print(f"╚═══════════════════════════════════════════╝{W}")
    
    L = instaloader.Instaloader()

    # Connexion requise pour extraire des listes
    user = input(f"\n{BOLD}{Y}[➤] Votre nom d'utilisateur : {W}{BOLD}")
    password = input(f"{BOLD}{Y}[➤] Votre mot de passe : {W}{BOLD}")
    
    try:
        print(f"\n{BOLD}{C}[*] Tentative de connexion...{W}")
        L.login(user, password)
        print(f"{BOLD}{G}[✔] Connecté en tant que @{user}{W}")
        
        target = input(f"\n{BOLD}{Y}[➤] Nom de la cible à extraire : {W}{BOLD}")
        print(f"{BOLD}{C}[*] Récupération du profil @{target}...{W}")
        
        profile = instaloader.Profile.from_username(L.context, target)
        
        # Création du fichier de résultat
        filename = f"followers_{target}.txt"
        with open(filename, "w") as f:
            print(f"{BOLD}{Y}[*] Extraction en cours (veuillez patienter)...{W}")
            for follower in profile.get_followers():
                f.write(f"{follower.username}\n")
                print(f"{BOLD}{G} [+] {follower.username}{W}")
        
        print(f"\n{BOLD}{G}═══════════════════════════════════════════")
        print(f" TERMINE ! {len(list(profile.get_followers()))} abonnés extraits.")
        print(f" Fichier : {filename}{W}")
        
    except Exception as e:
        print(f"\n{BOLD}{R}[✘] Erreur : {e}{W}")
    
    input(f"\n{BOLD}{C}[ Appuyez sur Entrée ]{W}")
    bot_engine()

# ... (le reste du code bot_engine reste identique)
