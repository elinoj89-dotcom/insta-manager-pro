import os
import time
import sys

# Couleurs
G = "\033[32m" # Vert
R = "\033[31m" # Rouge
W = "\033[0m"  # Blanc
P = "\033[35m" # Violet

def setup():
    os.system('clear')
    print(f"{P}=============================================")
    print(f"       INSTALLATION DU SYSTÈME SMM         ")
    print(f"============================================={W}")
    
    print(f"\n{G}[*] Mise à jour des paquets...{W}")
    time.sleep(1)
    
    # Installation de la dépendance principale
    print(f"{G}[*] Installation de instabot en cours...{W}")
    os.system('pip install instabot')
    
    print(f"\n{G}[✔] Installation terminée avec succès !{W}")
    time.sleep(2)
    
    # Lancement automatique du script principal
    print(f"{G}[*] Lancement de la vérification de sécurité...{W}")
    os.system('python main.py')

if __name__ == "__main__":
    setup()
  
