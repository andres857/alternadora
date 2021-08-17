from paho.mqtt import client as mqtt_client
from broker import index
from Control import ir, system
import json, time, lirc

broker = index.options['broker']
port = int(index.options['port'])
client_id = 'controlIR_imbanaco_01'
username = index.options['username']
password = index.options['password']

# subscriber topics
request = index.topics['subscriber'][0]
channel = index.topics['subscriber'][1]

# publish topics
status = index.topics['publish'][0]
currentStreaming = index.topics['publish'][1]
print(f'Publish on topics \n {status} \n {currentStreaming}')



# Connect to Broker
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

    # receive messages from the broker
    def on_message(client,userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        message = json.loads(msg.payload.decode())

        if msg.topic == request:
            if message['status'] == 'get':
                print(f'Publicando estados en el topic {status}')
                client.publish(status, json.dumps(system.statusAlternadora()))
            else:
                print('[ Broker - subscriber : peticiones no validas ]')

        elif msg.topic == channel:
            
            if message['channel'] == 'Imbanaco tv':
                print(f'Nada que hacer')
                client.publish(currentStreaming, json.dumps({"currentStreaming": "Imbanaco tv"}),qos=0, retain=True)

            elif message['channel'] == 'caracol':
                print(f'Cambiando canal a caracol')
                time.sleep(0.2)
                ir.changeChannel('caracol')
                time.sleep(0.2)
                print('simular publicando estados en el topic currentStreaming')
                print(currentStreaming)
                client.publish(currentStreaming, json.dumps({"currentStreaming": "caracol"}),qos=0, retain=True)

            elif message['channel'] == 'rcn':
                print(f'Simulando cambiar canal a rcn')
                time.sleep(0.2)
                ir.changeChannel('rcn')
                time.sleep(0.2)
                print('simular publicando estados en el topic currentStreaming')
                print(currentStreaming)
                client.publish(currentStreaming, json.dumps({"currentStreaming": "rcn"}),qos=0, retain=True)

            elif message['channel'] == 'teleantioquia':
                print(f'Simulando cambiar canal a teleantioquia')
                time.sleep(0.2)
                ir.changeChannel('teleantioquia')
                time.sleep(0.2)
                print('simular publicando estados en el topic currentStreaming')
                print(currentStreaming)
                client.publish(currentStreaming, json.dumps({"currentStreaming": "teleantioquia"}),qos=0, retain=True)

            elif message['channel'] == 'history':
                print(f'Simulando cambiar canal a history')
                time.sleep(0.2)
                ir.changeChannel('history')
                time.sleep(0.2)
                print('simular publicando estados en el topic currentStreaming')
                print(currentStreaming)
                client.publish(currentStreaming, json.dumps({"currentStreaming": "history"}),qos=0, retain=True)
            
            elif message['channel'] == 'natgeo':
                print(f'Simulando cambiar canal a natgeo')
                time.sleep(0.2)
                ir.changeChannel('natgeo')
                time.sleep(0.2)
                print('simular publicando estados en el topic currentStreaming')
                print(currentStreaming)
                client.publish(currentStreaming, json.dumps({"currentStreaming": "natgeo"}),qos=0, retain=True)

            elif message['channel'] == 'discovery':
                print(f'Simulando cambiar canal a discovery')
                time.sleep(0.2)
                ir.changeChannel('discovery')
                time.sleep(0.2)
                print('simular publicando estados en el topic currentStreaming')
                print(currentStreaming)
                client.publish(currentStreaming, json.dumps({"currentStreaming": "discovery"}),qos=0, retain=True)
           
            elif message['channel'] == 'fox':
                print(f'Simulando cambiar canal a fox')
                time.sleep(0.2)
                ir.changeChannel('fox')
                time.sleep(0.2)
                print('simular publicando estados en el topic currentStreaming')
                print(currentStreaming)
                client.publish(currentStreaming, json.dumps({"currentStreaming": "fox"}),qos=0, retain=True)
            
            elif message['channel'] == 'win':
                print(f'Simulando cambiar canal a win')
                time.sleep(0.2)
                ir.changeChannel('win')
                time.sleep(0.2)
                print('simular publicando estados en el topic currentStreaming')
                print(currentStreaming)
                client.publish(currentStreaming, json.dumps({"currentStreaming": "win"}),qos=0, retain=True)

            elif message['channel'] == 'espn':
                print(f'Simulando cambiar canal a espn')
                time.sleep(0.2)
                ir.changeChannel('espn')
                time.sleep(0.2)
                print('simular publicando estados en el topic currentStreaming')
                print(currentStreaming)
                client.publish(currentStreaming, json.dumps({"currentStreaming": "espn"}),qos=0, retain=True)

            elif message['channel'] == 'espn2':
                print(f'Simulando cambiar canal a espn2')
                time.sleep(0.2)
                ir.changeChannel('espn2')
                time.sleep(0.2)
                print('simular publicando estados en el topic currentStreaming')
                print(currentStreaming)
                client.publish(currentStreaming, json.dumps({"currentStreaming": "espn2"}),qos=0, retain=True)
            
            elif message['channel'] == 'tnt':
                print(f'Simulando cambiar canal a tnt')
                time.sleep(0.2)
                ir.changeChannel('tnt')
                time.sleep(0.2)
                print('simular publicando estados en el topic currentStreaming')
                print(currentStreaming)
                client.publish(currentStreaming, json.dumps({"currentStreaming": "tnt"}),qos=0, retain=True)
            
            elif message['channel'] == 'space':
                print(f'Simulando cambiar canal a space')
                time.sleep(0.2)
                ir.changeChannel('space')
                time.sleep(0.2)
                print('simular publicando estados en el topic currentStreaming')
                print(currentStreaming)
                client.publish(currentStreaming, json.dumps({"currentStreaming": "space"}),qos=0, retain=True)

            elif message['channel'] == 'studio':
                print(f'Simulando cambiar canal a studio')
                time.sleep(0.2)
                ir.changeChannel('studio')
                time.sleep(0.2)
                print('simular publicando estados en el topic currentStreaming')
                print(currentStreaming)
                client.publish(currentStreaming, json.dumps({"currentStreaming": "studio"}),qos=0, retain=True)

            elif message['channel'] == 'warner':
                print(f'Simulando cambiar canal a warner')
                time.sleep(0.2)
                ir.changeChannel('warner')
                time.sleep(0.2)
                print('simular publicando estados en el topic currentStreaming')
                print(currentStreaming)
                client.publish(currentStreaming, json.dumps({"currentStreaming": "warner"}),qos=0, retain=True)

            elif message['channel'] == 'cnetwork':
                print(f'Simulando cambiar canal a cnetwork')
                time.sleep(0.2)
                ir.changeChannel('cnetwork')
                time.sleep(0.2)
                print('simular publicando estados en el topic currentStreaming')
                print(currentStreaming)
                client.publish(currentStreaming, json.dumps({"currentStreaming": "cnetwork"}),qos=0, retain=True)
            
            elif message['channel'] == 'cnetwork':
                print(f'Simulando cambiar canal a cnetwork')
                time.sleep(0.2)
                ir.changeChannel('cnetwork')
                time.sleep(0.2)
                print('simular publicando estados en el topic currentStreaming')
                print(currentStreaming)
                client.publish(currentStreaming, json.dumps({"currentStreaming": "cnetwork"}),qos=0, retain=True)

            elif message['channel'] == 'disney':
                print(f'Simulando cambiar canal a disney')
                time.sleep(0.2)
                ir.changeChannel('disney')
                time.sleep(0.2)
                print('simular publicando estados en el topic currentStreaming')
                print(currentStreaming)
                client.publish(currentStreaming, json.dumps({"currentStreaming": "disney"}),qos=0, retain=True)
            
            elif message['channel'] == 'nick':
                print(f'Simulando cambiar canal a nick')
                time.sleep(0.2)
                ir.changeChannel('nick')
                time.sleep(0.2)
                print('simular publicando estados en el topic currentStreaming')
                print(currentStreaming)
                client.publish(currentStreaming, json.dumps({"currentStreaming": "nick"}),qos=0, retain=True)

            elif message['channel'] == 'discoverykids':
                print(f'Simulando cambiar canal a discoverykids')
                time.sleep(0.2)
                ir.changeChannel('discoverykids')
                time.sleep(0.2)
                print('simular publicando estados en el topic currentStreaming')
                print(currentStreaming)
                client.publish(currentStreaming, json.dumps({"currentStreaming": "discoverykids"}),qos=0, retain=True)    

            else:
                print('[ Broker - subscriber : peticiones no validas ]')
        
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()
