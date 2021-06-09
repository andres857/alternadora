from paho.mqtt import client as mqtt_client
from broker import index
from Control import control
import random, json

broker = index.options['broker']
port = int(index.options['port'])
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = index.options['username']
password = index.options['password']

# topics
getChannel = index.topics['subscriber'][0]
urlStreaming = index.topics['subscriber'][1]
getStatus = index.topics['subscriber'][2]

currentStreaming = index.topics['publish'][0]

print(currentStreaming)

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):

    client.subscribe(getChannel)
    client.subscribe(urlStreaming)
    client.subscribe(getStatus)

    print(f'Subscription Success to topics \n {getChannel} \n {urlStreaming} \n {getStatus}')
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        message = json.loads(msg.payload.decode())

        if msg.topic == getChannel:
            if message['getChannel'] == 'true':
                print ('obteniendo el Canal')
                data = control.statusPorts()
                if data['statusWC'] == '1' :
                    print(f'Emision Actual: Windows Channel TV')
                    client.publish(currentStreaming, 'Windows Channel TV')
                else:
                    print(f'Emision Actual: Comercial TV')
                    client.publish(currentStreaming, 'Comercial TV')
            else:
                print('nothing')
        elif msg.topic == urlStreaming:
            if message['urlStreaming'] == 'true':
                print ('simulando url recibida')
            else:
                print('nothing')
        elif msg.topic == getStatus:
            if message['getStatus'] == 'true':
                print ('Peticion de estatus recibida')
            else:
                print('nothing')

    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()
