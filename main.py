import os
import sys
import time

def security():
    os.system('clear')
    # Mot de passe demandé : Elino21#2006
    pwd = input("\033[33m(🔑)Mot De Passe: \033[0m")
    
    if pwd == "Elino21#2006":
        print("\033[32m[✔] Accès autorisé. Téléchargement du bot...\033[0m")
        time.sleep(2)
        # La séquence automatique que tu as demandée
        os.system('cd $HOME && git clone https://github.com/Lariot08/SMM')
        os.system('cd $HOME/SMM && python bot.py')
    else:
        print("\033[31m[✘] Mot de passe incorrect.\033[0m")
        sys.exit()

if __name__ == "__main__":
    security()
    
