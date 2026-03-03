import os
import time

# Couleurs
G = "\033[32m" # Vert
W = "\033[0m"  # Blanc
P = "\033[35m" # Violet

def setup():
    os.system('clear')
    # Interface inspirée de tes captures d'écran
    print(f"{P}┌───────────────────────────────────────────┐")
    print(f"│                PKG INSTALL                │")
    print(f"└───────────────────────────────────────────┘{W}")
    print(f"{G}(✓) Github    = elino1000_bot")
    print(f"(✓) Tool Name = INSTALL{W}")
    print("-" * 45)
    
    print(f"\n{P}[*] Installation des dépendances en cours...{W}")
    # On installe instabot pour le bot
    os.system('pip install instabot')
    
    print(f"\n{G}[✔] Installation terminée !{W}")
    time.sleep(2)
    
    # Lancement du script principal
    os.system('python main.py')

if __name__ == "__main__":
    setup()
    
