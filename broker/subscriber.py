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
getChannel = index.topics['subscriber'][0]
channel = index.topics['subscriber'][1]
getStatus = index.topics['subscriber'][2]


status = index.topics['publish'][0]


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
    client.subscribe(channel)
    client.subscribe(getStatus)


    print(f'Subscription Success to topics \n {getChannel} \n {getStatus} \n {channel}')
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        message = json.loads(msg.payload.decode())

        if msg.topic == getStatus:
            if message['status'] == 'get':
                print('simular publicando estados')
                # statusdict = system.statusAlternadora()
                # statusjson = json.dumps(statusdict)

                client.publish(status, json.dumps(system.statusAlternadora()))

        elif msg.topic == channel:
            if message['channel'] == 'caracol':
                print(f'Simulando cambiar canal a caracol')
                time.sleep(0.2)
                ir.changeChannel('caracol')
            elif message['channel'] == 'rcn':
                print(f'Simulando cambiar canal a rcn')
                time.sleep(0.2)
                ir.changeChannel('rcn')
            elif message['channel'] == 'colombia':
                print(f'Simulando cambiar canal a Senal Colombia')
                time.sleep(0.2)
                ir.changeChannel('colombia')
            elif message['channel'] == 'imbanaco':
                ir.changeChannel('imbanaco')

            else:
                print('nothing')

    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()
