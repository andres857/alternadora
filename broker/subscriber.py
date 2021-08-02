from paho.mqtt import client as mqtt_client
from broker import index
# from Control import control
from Control import ir, system
import random, json, time, lirc


broker = index.options['broker']
port = int(index.options['port'])
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = index.options['username']
password = index.options['password']

# topics

request = index.topics['subscriber'][0]
channel = index.topics['subscriber'][1]



status = index.topics['publish'][0]
currentStreaming = index.topics['publish'][1]

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


    client.subscribe(request)
    client.subscribe(channel)


    print(f'Subscription Success to topics \n {request} \n {channel}')
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        message = json.loads(msg.payload.decode())

        if msg.topic == request:
            if message['status'] == 'get':
                print('simular publicando estados')
                client.publish(status, json.dumps(system.statusAlternadora()))

        elif msg.topic == channel:
            if message['channel'] == 'caracol':
                print(f'Simulando cambiar canal a caracol')
                time.sleep(0.2)
                ir.changeChannel('caracol')
                time.sleep(0.2)
                client.publish(currentStreaming, json.dumps({"currentStreaming": "caracol"}))
            elif message['channel'] == 'rcn':
                print(f'Simulando cambiar canal a rcn')
                time.sleep(0.2)
                ir.changeChannel('rcn')
                time.sleep(0.2)
                print(currentStreaming)
                client.publish(currentStreaming, json.dumps({"currentStreaming": "rcn"}))
            elif message['channel'] == 'scolombia':
                print(f'Simulando cambiar canal a Senal Colombia')
                time.sleep(0.2)
                ir.changeChannel('colombia')
                time.sleep(0.2)
                client.publish(currentStreaming, json.dumps({"currentStreaming": "senalcolombia"}))
            elif message['channel'] == 'imbanacotv':
                #ir.changeChannel('imbanaco')
                print('canal imbanaco')
                client.publish(currentStreaming, json.dumps({"currentStreaming": "imbanacotv"}))

            else:
                print('nothing')

    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()
