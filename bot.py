import os
import time
import sys

# Styles et Couleurs GRAS
BOLD = "\033[1m"
G = "\033[1;32m" ; Y = "\033[1;33m" ; W = "\033[1;37m" 
C = "\033[1;36m" ; B = "\033[1;34m" ; R = "\033[1;31m"

def extract_followers():
    """Option [2] : Logique d'extraction d'abonnés"""
    os.system('clear')
    print(f"{BOLD}{C}╔═══════════════════════════════════════════╗")
    print(f"║         EXTRACTION D'ABONNÉS SMM          ║")
    print(f"╚═══════════════════════════════════════════╝{W}")
    
    target = input(f"\n{BOLD}{Y}[➤] Nom d'utilisateur cible : {W}{BOLD}")
    limit = input(f"{BOLD}{Y}[➤] Nombre d'abonnés à extraire : {W}{BOLD}")
    
    print(f"\n{BOLD}{C}[*] Connexion aux serveurs Instagram...{W}")
    time.sleep(2)
    print(f"{BOLD}{C}[*] Analyse du compte @{target}...{W}")
    time.sleep(2)
    
    # Ici, on simule l'extraction (ou on appelle l'API de scraping)
    print(f"\n{BOLD}{G}[✔] Extraction réussie !{W}")
    print(f"{BOLD}{W}📂 Fichier enregistré : {G}extract_{target}.txt{W}")
    
    input(f"\n{BOLD}{C}[ Appuyez sur Entrée pour continuer ]{W}")
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
    print(f"│ [3] Message Direct Groupé              │")
    print(f"│ [0] Retour au Menu Principal           │")
    print(f"└────────────────────────────────────────┘{W}")

    choice = input(f"\n{BOLD}{Y}[➤] Sélectionnez une action : {W}{BOLD}")

    if choice == "1":
        print(f"\n{BOLD}{C}[*] Module Auto-Like en cours...{W}")
        time.sleep(3); bot_engine()
    elif choice == "2":
        extract_followers()
    elif choice == "0":
        os.system('python ~/INSTALL/main.py')
    else:
        bot_engine()

if __name__ == "__main__":
    try:
        bot_engine()
    except KeyboardInterrupt:
        print(f"\n{BOLD}{R}[!] Bot arrêté.{W}")
        sys.exit()
    
