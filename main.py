import os
import sys
import hashlib
import requests

BOLD = "\033[1m"
B = "\033[1;34m"
Y = "\033[1;33m"
G = "\033[1;32m"
P = "\033[1;35m"
R = "\033[1;31m"
W = "\033[1;37m"

def show_menu():
    os.system('clear')
    print(f"{BOLD}{B}  ██████  ███    ███ ███    ███ \n ██       ████  ████ ████  ████ \n   ████   ██ ████ ██ ██ ████ ██ \n       ██ ██  ██  ██ ██  ██  ██ \n  ██████  ██      ██ ██      ██{W}")
    print(f"{BOLD}{P}┌───────────────────────────────────────────┐")
    print(f"│ {Y}[1] Démarrer le Bot                       {P}│")
    print(f"│ {Y}[8] Mettre à jour                         {P}│")
    print(f"│ {R}[0] Quitter                               {P}│")
    print(f"└───────────────────────────────────────────┘{W}")
    
    choice = input(f"\n{BOLD}{B}[➤] Choix : {W}{BOLD}")
    if choice == "1" or choice == "8":
        # ICI : On lance l'update qui va ensuite demander le MDP
        os.system('python ~/insta-manager-pro/update.py')
    elif choice == "0":
        sys.exit()

if __name__ == "__main__":
    show_menu()
    
