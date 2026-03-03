import os
import time
import sys

# Couleurs
P = "\033[35m" # Violet
G = "\033[32m" # Vert
W = "\033[0m"  # Blanc
R = "\033[31m" # Rouge

def loader():
    os.system('clear')
    # Texte de ton screenshot
    print(f"{P}Veuillez patienter, installation d'Instagram en cours...{W}")
    print("-" * 45)
    
    # Barre de progression animée
    for i in range(1, 101):
        time.sleep(0.05)
        sys.stdout.write(f"\r{G}[*] Configuration des paquets : {i}%")
        sys.stdout.flush()
    
    print(f"\n\n{G}[✔] Instagram est prêt !{W}")
    time.sleep(1.5)

def main():
    loader()
    # Après le chargement, on lance automatiquement le bot final
    # Assure-toi que ton bot se nomme bot.py ou main.py dans ce dossier
    if os.path.exists("bot.py"):
        os.system('python bot.py')
    else:
        print(f"{R}[!] Erreur : bot.py introuvable dans le dossier.{W}")

if __name__ == "__main__":
    main()
  
