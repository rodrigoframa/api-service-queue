import redis
import json
import os
from bottle import Bottle, request


class Sender(Bottle):
    def __init__(self):
        super().__init__()
        self.route('/', method='POST', callback=self.send)
        
        redis_host = os.getenv('REDIS_HOST', 'queue')
        self.fila = redis.StrictRedis(host=redis_host, port=6379, db=0)

    def register_queue(self, id_agendamento, usuario):
        agendamento = {'id': id_agendamento, 'usuario': usuario}        
        self.fila.rpush('escala', json.dumps(agendamento))
        print('escala na fila 2!', agendamento)

    def send(self):
        servico = request.forms.get('servico')
        id_agendamento = request.forms.get('id_agendamento')
        usuario = request.forms.get('usuario')

        self.register_queue(id_agendamento, usuario)    
        return 'Agendamento do serviço {} enfileirado pelo usuário {}'.format(servico, usuario)

if __name__ == '__main__':
    sender = Sender()
    sender.run(host='0.0.0.0', port=8000, debug=True)