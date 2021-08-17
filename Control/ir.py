import lirc,time
from channels import gChannels  
clientIR = lirc.Client()

decodificador = 'emcali'

channels = gChannels()

def changeChannel(channel):
    try:
        for tecla in channels[f'{channel}']:
            print (tecla)
            clientIR.send_once(decodificador, tecla)
            time.sleep(5)
        time.sleep(3.5)
    except:
        print(f'[ir - Error al enviar las senales infrarojas]')

    
