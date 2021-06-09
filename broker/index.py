#!/usr/bin/python3
import random

clientPlayer = 'imbanaco'
sede = 'principal'
idPlayer = 'rjhgejhge'
client_id = f'python-mqtt-{random.randint(0, 1000)}'

options = {
    'broker' : 'broker.windowschannel.us',
    'port' : 1883,
    # generate client ID with pub prefix randomly
    'client_id' : {client_id},
    'username' : 'emqx',
    'password' : 'public',
}

topics = {
    'subscriber': [
        f'{clientPlayer}/{sede}/alternadora/{idPlayer}/getChannel',
        f'{clientPlayer}/{sede}/alternadora/{idPlayer}/urlStreaming',
        f'{clientPlayer}/{sede}/alternadora/{idPlayer}/getStatus',
        ],
    'publish':[
        f'{clientPlayer}/{sede}/alternadora/{idPlayer}/currentStreaming',
        f'{clientPlayer}/{sede}/alternadora/{idPlayer}/status'
    ]
}

# broker = index.options['broker']
# port = 1883
# client_id = 5456464
# username = index.options['username']
# password = index.options['password']
#
# topic = index.topics['subscriber'][0]
#
#
# print(password)
