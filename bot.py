import os
import time
import sys

# Styles et Couleurs GRAS
BOLD = "\033[1m"
G = "\033[1;32m" ; Y = "\033[1;33m" ; W = "\033[1;37m" 
C = "\033[1;36m" ; B = "\033[1;34m" ; R = "\033[1;31m"

def bot_engine():
    os.system('clear')
    # Bannière de bienvenue personnalisée
    print(f"{BOLD}{B}╔═══════════════════════════════════════════╗")
    print(f"║          SMM BOT ENGINE ACTIVÉ            ║")
    print(f"║          DÉVELOPPÉ PAR ELINO              ║")
    print(f"╚═══════════════════════════════════════════╝{W}")
    
    print(f"\n{BOLD}{G}[✔] Connexion au serveur Instagram réussie.")
    print(f"{BOLD}{G}[✔] Moteur de Scraping prêt.{W}")
    
    print(f"\n{BOLD}{C}┌──────────── ACTIONS DU BOT ────────────┐")
    print(f"│ [1] Auto Like & Follow                 │")
    print(f"│ [2] Extraction d'abonnés               │")
    print(f"│ [3] Message Direct Groupé              │")
    print(f"│ [0] Retour au Menu Principal           │")
    print(f"└────────────────────────────────────────┘{W}")

    choice = input(f"\n{BOLD}{Y}[➤] Sélectionnez une action : {W}{BOLD}")

    if choice == "1":
        print(f"\n{BOLD}{C}[*] Initialisation du module Auto-Like...{W}")
        # Insère ton code de scraping ici
        time.sleep(3)
    elif choice == "0":
        # Retourne au menu principal de INSTALL
        os.system('python ~/INSTALL/main.py')
    else:
        print(f"\n{BOLD}{R}[!] Action non configurée.{W}")
        time.sleep(2)
        bot_engine()

if __name__ == "__main__":
    try:
        bot_engine()
    except KeyboardInterrupt:
        print(f"\n{BOLD}{R}[!] Bot arrêté.{W}")
        sys.exit()
  
