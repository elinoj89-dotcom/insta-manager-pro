import os
import time
import sys
import instaloader
import getpass  # Pour masquer le mot de passe

# Styles et Couleurs GRAS
BOLD = "\033[1m"
G = "\033[1;32m" ; Y = "\033[1;33m" ; W = "\033[1;37m" 
C = "\033[1;36m" ; B = "\033[1;34m" ; R = "\033[1;31m"

def extract_followers():
    os.system('clear')
    print(f"{BOLD}{C}╔═══════════════════════════════════════════╗")
    print(f"║         CONNEXION ULTRA-SÉCURISÉE         ║")
    print(f"╚═══════════════════════════════════════════╝{W}")
    
    L = instaloader.Instaloader()
    
    user = input(f"\n{BOLD}{Y}[➤] Votre nom d'utilisateur : {W}{BOLD}")
    
    # ICI : On utilise getpass au lieu de input
    # Note : Rien ne s'affichera à l'écran quand l'utilisateur tape, c'est normal !
    password = getpass.getpass(f"{BOLD}{Y}[➤] Votre mot de passe (invisible) : {W}{BOLD}")
    
    try:
        print(f"\n{BOLD}{C}[*] Authentification en cours...{W}")
        L.login(user, password)
        print(f"{BOLD}{G}[✔] Accès autorisé !{W}")
        
        target = input(f"\n{BOLD}{Y}[➤] Nom de la cible : {W}{BOLD}")
        limit = int(input(f"{BOLD}{Y}[➤] Limite d'extraction : {W}{BOLD}"))
        
        profile = instaloader.Profile.from_username(L.context, target)
        filename = f"followers_{target}.txt"
        count = 0
        
        print(f"\n{BOLD}{B}[▶] Extraction lancée...{W}")
        
        with open(filename, "w") as f:
            for follower in profile.get_followers():
                if count >= limit: break
                f.write(f"{follower.username}\n")
                count += 1
                # Barre de progression
                fraction = count / limit
                bar = int(30 * fraction) * "█" + (30 - int(30 * fraction)) * "-"
                print(f"{BOLD}{C}[{bar}] {int(fraction*100)}%{W}", end="\r")
                sys.stdout.flush()
                time.sleep(0.1)

        print(f"\n\n{BOLD}{G}[✔] TERMINÉ ! {count} noms enregistrés.{W}")
        # Alerte sonore via Termux-API
        os.system('termux-vibrate -d 500')
        os.system('termux-tts-speak "Opération réussie Elino"')
        
    except Exception as e:
        print(f"\n{BOLD}{R}[✘] Erreur de connexion : {e}{W}")
    
    input(f"\n{BOLD}{C}[ Appuyez sur Entrée ]{W}")
    bot_engine()

# ... (le reste du code bot_engine)
