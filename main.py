from instabot import Bot
import time
import random
from datetime import datetime
import sys

# --- CONFIGURATION DU STYLE ---
G = "\033[32m" # Vert
R = "\033[31m" # Rouge
W = "\033[0m"  # Blanc
Y = "\033[33m" # Jaune
B = "\033[34m" # Bleu
P = "\033[35m" # Violet

# --- TON NOUVEAU MOT DE PASSE ---
PASSWORD_SCRIPT = "Elino21#2006"

def get_time():
    return datetime.now().strftime("[%H:%M:%S]")

def login_script():
    print(f"{P}=============================================")
    print(f"       SYSTÈME DE SÉCURITÉ ACTIVE          ")
    print(f"       PASSWORD PROTECTED BY ELINO         ")
    print(f"============================================={W}")
    
    # Demande du mot de passe
    access = input(f"{get_time()} {Y}[?] Entrez le mot de passe d'accès : {W}")
    
    if access == PASSWORD_SCRIPT:
        print(f"{get_time()} {G}[✔] Mot de passe correct !{W}")
        print(f"{get_time()} {G}[*] Initialisation du système...{W}\n")
        time.sleep(1.5)
    else:
        print(f"{get_time()} {R}[✘] Accès refusé : Mot de passe invalide.{W}")
        sys.exit()

def banner():
    print(f"{B}=============================================")
    print(f"       INSTA-MANAGER-PRO v2.6              ")
    print(f"   LIKE | FOLLOW | COMMENT | SECURE        ")
    print(f"============================================={W}\n")

def demarrer_bot():
    # 1. Vérification du mot de passe Elino21#2006
    login_script()
    
    # 2. Affichage de la bannière pro
    banner()
    
    # --- TA CONFIGURATION INSTAGRAM ---
    bot = Bot()
    INSTA_USER = "ton_pseudo_instagram"
    INSTA_PASS = "ton_mot_de_passe"

    print(f"{get_time()} {Y}[*] Connexion à Instagram en cours...{W}")
    
    try:
        # Tentative de login Instagram
        if bot.login(username=INSTA_USER, password=INSTA_PASS):
            print(f"{get_time()} {G}[✔] Session Instagram établie : {INSTA_USER}{W}")
        else:
            print(f"{get_time()} {R}[✘] Échec de connexion Instagram.{W}")
            return
    except Exception as e:
        print(f"{get_time()} {R}[!] Erreur de serveur : {e}{W}")
        return

    # --- ACTIONS AUTOMATIQUES ---
    hashtag = "motivation"
    commentaires = ["Incroyable ! 🔥", "Très inspirant ✨", "Excellent travail ! 🙌"]
    
    # Récupération des publications
    medias = bot.get_hashtag_medias(hashtag)
    
    for i, media_id in enumerate(medias[:5]):
        print(f"\n{get_time()} {B}[Action {i+1}] Cible ID: {media_id}{W}")
        
        # Like
        bot.like(media_id)
        print(f"{get_time()} {G}[+] J'aime envoyé avec succès{W}")
        
        # Commentaire aléatoire
        bot.comment(media_id, random.choice(commentaires))
        print(f"{get_time()} {G}[+] Commentaire posté{W}")
        
        # Follow de l'auteur
        user_id = bot.get_media_owner(media_id)
        bot.follow(user_id)
        print(f"{get_time()} {G}[+] Utilisateur suivi : {user_id}{W}")

        # Pause pour éviter d'être détecté
        pause = random.randint(45, 90)
        print(f"{get_time()} {Y}[~] Pause de sécurité : {pause}s...{W}")
        time.sleep(pause)

    print(f"\n{get_time()} {G}[✔] Programme terminé. Toutes les tâches sont finies.{W}")

if __name__ == "__main__":
    demarrer_bot()
    
