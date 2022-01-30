
from config import *
import tweepy
import time
import random
import os

print('🌸 Inicializando 🌸', flush=True)

CONSUMER_KEY = api_key
CONSUMER_SECRET = api_secret
ACCESS_KEY = access_token
ACCESS_SECRET = token_secret

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_id.txt'

lista = ['bi bu bu bop', 'Hola que tal :p',
         'simio', 'random.choice(mensajes)', 'lorem ipsum dolor sit amet, consectetur adipiscing elit.',
         'I dont know about you But Im feeling 22', 'a', '@kannssai ayuda no se que decir',
         'es que es lo mismo wey, es exactamente, es una construcción intersubjetiva a la que le adjudicas un valor intrínseco y la persigues, osea el hecho de que la gente se forme para tocar una piedra wey es lo mismo a que la gente se forme a tomarse una foto con un espejo, es lo mismo',
         'apagame']


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
    last_id = string_lastid(FILE_NAME)
    mentions = api.mentions_timeline(last_id)
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.text, flush=True)
        last_id = mention.id
        guarda_lastid(last_id, FILE_NAME)
        print('> Me mencionaron!', flush=True)
        print('> Respondiendo...', flush=True)
        api.update_status('@' + mention.user.screen_name +
                          ' ' + random.choice(lista), mention.id)


while True:
    reply()
    time.sleep(15)
