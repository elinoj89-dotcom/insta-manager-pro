from instabot import Bot
import sys
import time

# Ton mot de passe défini
PASSWORD_SCRIPT = "Elino21#2006"

def login_check():
    print(f"\033[35m[SYSTEM] Vérification d'accès requis... \033[0m")
    pwd = input("\033[33m[?] Mot de passe : \033[0m")
    
    if pwd == PASSWORD_SCRIPT:
        print("\033[32m[✔] Accès accordé. Bienvenue Elino.\033[0m")
        time.sleep(1)
    else:
        print("\033[31m[✘] Accès refusé.\033[0m")
        sys.exit()

# ... (Le reste du code de ton bot que nous avons écrit précédemment) ...
