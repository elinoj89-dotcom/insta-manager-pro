import os
import time
import sys
import instaloader

# Styles et Couleurs GRAS
BOLD = "\033[1m"
G = "\033[1;32m" ; Y = "\033[1;33m" ; W = "\033[1;37m" 
C = "\033[1;36m" ; B = "\033[1;34m" ; R = "\033[1;31m"

def alert_user():
    """Fait vibrer et biper Termux (nécessite termux-api)"""
    os.system('termux-vibrate -d 500') # Vibre 500ms
    os.system('termux-tts-speak "Extraction terminée avec succès"')
    # Si termux-api n'est pas là, on fait un bip standard
    print("\a") 

def progress_bar(current, total, bar_length=30):
    fraction = current / total
    arrow = int(fraction * bar_length - 1) * "=" + ">"
    padding = int(bar_length - len(arrow)) * " "
    print(f"{BOLD}{C}[{G}{arrow}{padding}{C}] {int(fraction*100)}% {W}", end="\r")
    sys.stdout.flush()

def extract_followers():
    os.system('clear')
    print(f"{BOLD}{C}╔═══════════════════════════════════════════╗")
    print(f"║         EXTRACTION SMM PRO + ALERTE       ║")
    print(f"╚═══════════════════════════════════════════╝{W}")
    
    L = instaloader.Instaloader()
    user = input(f"\n{BOLD}{Y}[➤] Votre nom d'utilisateur : {W}{BOLD}")
    password = input(f"{BOLD}{Y}[➤] Votre mot de passe : {W}{BOLD}")
    
    try:
        print(f"\n{BOLD}{C}[*] Connexion sécurisée...{W}")
        L.login(user, password)
        
        target = input(f"\n{BOLD}{Y}[➤] Nom de la cible : {W}{BOLD}")
        limit = int(input(f"{BOLD}{Y}[➤] Limite d'extraction : {W}{BOLD}"))
        
        profile = instaloader.Profile.from_username(L.context, target)
        filename = f"followers_{target}.txt"
        count = 0
        
        print(f"\n{BOLD}{B}[▶] Extraction en cours...{W}")
        
        with open(filename, "w") as f:
            for follower in profile.get_followers():
                if count >= limit: break
                f.write(f"{follower.username}\n")
                count += 1
                progress_bar(count, limit)
                time.sleep(0.2)

        # SIGNAL DE FIN
        print(f"\n\n{BOLD}{G}[✔] TERMINE ! Fichier : {filename}{W}")
        alert_user()
        
    except Exception as e:
        print(f"\n{BOLD}{R}[✘] Erreur : {e}{W}")
    
    input(f"\n{BOLD}{C}[ Appuyez sur Entrée ]{W}")
    bot_engine()

def bot_engine():
    os.system('clear')
    print(f"{BOLD}{B}╔═══════════════════════════════════════════╗")
    print(f"║          SMM BOT ENGINE ACTIVÉ            ║")
    print(f"║          DÉVELOPPÉ PAR ELINO              ║")
    print(f"╚═══════════════════════════════════════════╝{W}")
    
    print(f"\n{BOLD}{C}┌──────────── ACTIONS DU BOT ────────────┐")
    print(f"│ [1] Auto Like & Follow                 │")
    print(f"│ [2] Extraction d'abonnés               │")
    print(f"│ [0] Retour au Menu Principal           │")
    print(f"└────────────────────────────────────────┘{W}")

    choice = input(f"\n{BOLD}{Y}[➤] Sélectionnez une action : {W}{BOLD}")
    if choice == "2":
        extract_followers()
    elif choice == "0":
        os.system('python ~/INSTALL/main.py')
    else:
        bot_engine()

if __name__ == "__main__":
    bot_engine()
    
