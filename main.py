from instabot import Bot
import time
import random
from datetime import datetime

# Couleurs pour le terminal
G = "\033[32m" # Vert (Succès)
R = "\033[31m" # Rouge (Erreur)
W = "\033[0m"  # Blanc (Reset)
Y = "\033[33m" # Jaune (Attente)
B = "\033[34m" # Bleu (Info)

bot = Bot()

def get_time():
    return datetime.now().strftime("[%H:%M:%S]")

def banner():
    print(f"{B}{'='*45}")
    print(f"       INSTA-MANAGER-PRO v1.2         ")
    print(f"   LIKE | FOLLOW | COMMENT | SECURE   ")
    print(f"{'='*45}{W}\n")

def demarrer_bot():
    banner()
    
    # --- TA CONFIGURATION ---
    USERNAME = "ton_pseudo_instagram"
    PASSWORD = "ton_mot_de_passe"

    print(f"{get_time()} {Y}[*] Connexion en cours...{W}")
    
    try:
        if bot.login(username=USERNAME, password=PASSWORD):
            print(f"{get_time()} {G}[✔] Connecté en tant que : {USERNAME}{W}")
        else:
            print(f"{get_time()} {R}[✘] Échec de la connexion.{W}")
            return
    except Exception as e:
        print(f"{get_time()} {R}[!] Erreur système : {e}{W}")
        return

    # --- PARAMÈTRES DES ACTIONS ---
    hashtag = "motivation"
    commentaires = ["Super post !", "Vraiment inspirant ✨", "Top !", "J'adore ça ! 🔥"]
    
    print(f"\n{get_time()} {B}[Action] Analyse du hashtag : #{hashtag}{W}")
    
    # Récupération des publications
    medias = bot.get_hashtag_medias(hashtag)
    
    for i, media_id in enumerate(medias[:5]): # On limite à 5 pour le test
        print(f"\n{get_time()} {B}--- Publication {i+1} ---{W}")
        
        # 1. LIKE
        if bot.like(media_id):
            print(f"{get_time()} {G}[+] J'aime Succès | Media ID: {media_id}{W}")
        
        # 2. COMMENTER
        commentaire = random.choice(commentaires)
        if bot.comment(media_id, commentaire):
            print(f"{get_time()} {G}[+] Commentaire envoyé : {commentaire}{W}")
            
        # 3. SUIVRE l'auteur (Follow)
        user_id = bot.get_media_owner(media_id)
        if bot.follow(user_id):
            print(f"{get_time()} {G}[+] Utilisateur suivi : {user_id}{W}")

        # Pause de sécurité pour éviter le bannissement
        pause = random.randint(30, 60)
        print(f"{get_time()} {Y}[~] Pause de sécurité : {pause}s...{W}")
        time.sleep(pause)

    print(f"\n{get_time()} {G}[✔] Toutes les actions ont été effectuées avec succès !{W}")

if __name__ == "__main__":
    demarrer_bot()
  
