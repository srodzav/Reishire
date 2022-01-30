# ⠄⠄⠄⢰⣧⣼⣯⠄⣸⣠⣶⣶⣦⣾⠄⠄⠄⠄⡀⠄⢀⣿⣿⠄⠄⠄⢸⡇⠄⠄
# ⠄⠄⠄⣾⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄⠸⢀⣿⠄
# ⠄⠄⢀⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿⣿⠄
# ⠄⠄⢸⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⠄
# ⠄⢀⢸⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠉⠋⣰
# ⠄⣼⣖⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⠇⢀⣤
# ⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴⣿⡗
# ⢀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄
# ⢸⣿⣦⣌⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄
# ⠘⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿⣿⣿⣵⣾⠃⠄
# ⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠃⠄⠄
# ⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁⠄⠄⠄
# ⠄⠄⠄⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁⠄⠄⠄⠄⠄
# ⠄⠄⠄⠄⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁⠄⠄⠄⠄⠄⢀⣠⣴
# ⣿⣿⣿⣶⣶⣮⣥⣒⠲⢮⣝⡿⣿⣿⡆⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⣠⣴⣿⣿⣿
# ==========================================
#  Title:  Twitter Bot
#  Author: sebrodzav
#  Date:   Jan 2022
# ==========================================

from config import *
import tweepy
import time
import random
import os
from bing_image_downloader import downloader

print('🌸 Inicializando 🌸', flush=True)

CONSUMER_KEY = api_key
CONSUMER_SECRET = api_secret
ACCESS_KEY = access_token
ACCESS_SECRET = token_secret

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_id.txt'


def string_lastid(file_name):
    f_read = open(file_name, 'r')
    last_id = int(f_read.read().strip())
    f_read.close()
    return last_id


def guarda_lastid(last_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_id))
    f_write.close()
    return


def reply():
    print('Buscando tweets...', flush=True)
    last_id = string_lastid(FILE_NAME)  # Lee el ultimo id
    mentions = api.mentions_timeline(last_id)  # Guarda las menciones
    for mention in reversed(mentions):  # Empieza por la primer mencion
        print(str(mention.id) + ' - ' + mention.text, flush=True)
        last_id = mention.id  # Guarda el id en last_id
        guarda_lastid(last_id, FILE_NAME)
        print('> Me mencionaron!', flush=True)
        txt = mention.text.lower()  # Conviete en lower el tweet
        split_txt = txt.split('@reishire ')  # Elimina el @Reishire
        txt = split_txt[1].strip()  # Queda la cadena sin el @Reishire
        downloader.download(txt, limit=1,  output_dir='dataset',
                            adult_filter_off=True, force_replace=False, timeout=60)  # Descarga la imagen
        print('> Intentando responder...')
        try:  # Intenta responder
            # Cambia de directorio al directorio descargado
            os.chdir("C:\\CODE\\Reishire\\dataset\\" + txt)
            filename = 'Image_1.jpg'
            status = '@' + mention.user.screen_name
            in_reply_to_status_id = mention.id
            api.update_with_media(
                filename, status, in_reply_to_status_id=in_reply_to_status_id)  # Twittea
            os.chdir("C:\\CODE\\Reishire")  # Regresa al directorio principal
            print('>> Respuesta exitosa!')
        except:  # Si no puede responder, regresa a la carpeta principal
            os.chdir("C:\\CODE\\Reishire")
            print('>> Ocurrio un error!')


while True:
    reply()
    time.sleep(10)
