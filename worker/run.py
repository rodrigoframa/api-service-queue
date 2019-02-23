import redis
import json
import os
from time import sleep
from random import randint 

if __name__ == '__main__':
    redis_host = os.getenv('REDIS_HOST', 'queue')
    r = redis.Redis(host=redis_host, port=6379, db=0)
    print('Aguardando agendamentos ...')
    while True:
        escala_agendada = json.loads(r.blpop('escala')[1])
        try:
            print('Gerar agendamento escala: {} , USUARIO: {} '.format(escala_agendada['id'], escala_agendada['usuario']))
            sleep(randint(15,45))
            print('Escala {} finalizada!'.format(escala_agendada['id']))
        except BaseException as e:
            print(e)

        