from instabot import Bot
import time
import random
from datetime import datetime
import sys

# Style et Couleurs
G = "\033[32m" # Vert
R = "\033[31m" # Rouge
W = "\033[0m"  # Blanc
Y = "\033[33m" # Jaune
P = "\033[35m" # Violet

def get_time():
    return datetime.now().strftime("[%H:%M:%S]")

def check_access():
    print(f"{P}=============================================")
    print(f"       SYSTÈME DE SÉCURITÉ SMM             ")
    print(f"============================================={W}")
    
    # Ton mot de passe spécifique
    password = input(f"{get_time()} {Y}[?] Password : {W}")
    
    if password == "Elino21#2006":
        print(f"{get_time()} {G}[✔] Accès autorisé. Bienvenue Elino.{W}\n")
        time.sleep(1)
    else:
        print(f"{get_time()} {R}[✘] Mot de passe incorrect.{W}")
        sys.exit()

def demarrer_bot():
    check_access()
    
    bot = Bot()
    # Met tes vrais identifiants ici (garde ton dépôt en PRIVÉ !)
    INSTA_USER = "ton_pseudo"
    INSTA_PASS = "ton_mot_de_passe"

    if not bot.login(username=INSTA_USER, password=INSTA_PASS):
        print(f"{get_time()} {R}[✘] Erreur de connexion Instagram.{W}")
        return

    hashtag = "motivation"
    medias = bot.get_hashtag_medias(hashtag)

    for i, media_id in enumerate(medias[:5]):
        # Interface calquée sur tes captures (Screenshot_20260302-143220.png)
        print(f"{W}[{i+1:02}] Username: {INSTA_USER} {G}[Succès]{W}")
        
        # Action Like
        bot.like(media_id)
        print(f"{G}[✔] J'aime Succès | + 1.1 CashCoins{W}")
        
        # Action Comment
        bot.comment(media_id, "Super post ! 🔥")
        print(f"{G}[✔] Commentaire Succès | + 0.5 CashCoins{W}")
        
        # Action Follow
        user_id = bot.get_media_owner(media_id)
        bot.follow(user_id)
        print(f"{G}[✔] Follow Succès | + 2.0 CashCoins{W}")

        # Pause de sécurité
        pause = random.randint(30, 60)
        print(f"{Y}[~] Pause : {pause}s...{W}")
        time.sleep(pause)

if __name__ == "__main__":
    demarrer_bot()
        
