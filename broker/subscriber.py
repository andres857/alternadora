from paho.mqtt import client as mqtt_client
from broker import index
from Control import control
from Control import ir
import random, json, time, lirc



broker = index.options['broker']
port = int(index.options['port'])
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = index.options['username']
password = index.options['password']

# topics
getChannel = index.topics['subscriber'][0]
changeStreaming = index.topics['subscriber'][1]
changeVolumen = index.topics['subscriber'][2]


currentStreaming = index.topics['publish'][0]

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
    client.subscribe(changeStreaming)
    client.subscribe(changeVolumen)

    print(f'Subscription Success to topics \n {getChannel} \n {changeStreaming} \n {changeVolumen}')
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        message = json.loads(msg.payload.decode())

        if msg.topic == getChannel:
            if message['getChannel'] == 'true':
                data = control.statusPorts()
                print('Estado antes de evaluar data')
                print(data)
                if data['statusWC'] == 1 :
                    print(f'Emision Actual: Canal Institucional')
                    client.publish(currentStreaming, json.dumps(data))
                else:
                    data = control.statusPorts()
                    time.sleep(0.2)
                    print(f'Emision Actual: Canal Comercial')
                    client.publish(currentStreaming, json.dumps(data))
            else:
                print('nothing')

        elif msg.topic == changeStreaming:
            if message['changeStreaming'] == 'true':
                control.alternateChannel()
                data = control.statusPorts()
                time.sleep(0.2)
                client.publish(currentStreaming, json.dumps(data))
            else:
                print('nothing')

        elif msg.topic == changeVolumen:
            if message['volumen'] == 'mas':
                print(f'Simulando subir Volumen')
                time.sleep(0.2)
                # ir.changeChannel('kalley','five','six')
                ir.onOff()
            else:
                print('nothing')

    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()
