import os
import time

# Couleurs Style Screenshot
P = "\033[35m" # Violet
G = "\033[32m" # Vert
W = "\033[0m"  # Blanc

def install_menu():
    os.system('clear')
    print(f"{P}┌───────────────────────────────────────────┐")
    print(f"│            INSTALLATION SYSTEM            │")
    print(f"└───────────────────────────────────────────┘{W}")
    print(f"{G}(✓) Github    = Lariot08")
    print(f"(✓) Tool Name = INSTALL{W}")
    print("-" * 45)
    print(f"{W}[1] ALL INSTALL PKG")
    print(f"[0] EXIT")
    
    choice = input(f"\n{P}[?] Choice: {W}")
    
    if choice == "1":
        print(f"\n{G}[*] Mise à jour et installation des paquets...{W}")
        os.system('pip install instabot --quiet')
        time.sleep(2)
        # On lance le verrou de sécurité
        os.system('python main.py')
    else:
        exit()

if __name__ == "__main__":
    install_menu()
    
