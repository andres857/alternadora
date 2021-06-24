#!/usr/bin/python3
import random

clientPlayer = 'imbanaco'
sede = 'principal'
idPlayer = 'b5c890'
client_id = f'imbanaco/controladora/{idPlayer}'

options = {
    'broker' : 'broker.windowschannel.us',
    'port' : 1883,
    'client_id' : {client_id},
    'username' : 'emqx',
    'password' : 'public',
}

topics = {
    'subscriber': [
        f'{clientPlayer}/{sede}/alternadora/{idPlayer}/getStatus',
        f'{clientPlayer}/{sede}/players/channel'
        ],
    'publish':[
        f'{clientPlayer}/{sede}/alternadora/{idPlayer}/status',
        f'{clientPlayer}/{sede}/currentStreaming',
    ]
}
