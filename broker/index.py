#!/usr/bin/python3

#<---------PORTS BROKER------------->
# - "1884:1883" # MQTT
# - "8884:8883" # MQTT/SSL
# - "7083:8083" # MQTT/WS
# - "8085:8084" # MQTT/WSS

client = 'imbanaco'
sede = 'principal'
idPlayer = 'b5c890'
client_id = f'imbanaco/managechannel/{idPlayer}'

options = {
    'broker' : 'brokerimbanaco.windowschannel.com',
    'port' : 1884,
    'client_id' : {client_id},
    'username' : 'emqx',
    'password' : 'public',
}

topics = {
    'subscriber': [
        f'{client}/{sede}/alternadora/{idPlayer}/request',
        f'{client}/{sede}/players/channel'
        ],
    'publish':[
        f'{client}/{sede}/alternadora/{idPlayer}/status',
        f'{client}/{sede}/currentStreaming',
    ]
}
