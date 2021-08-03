import lirc,time
from Control import control

clientIR = lirc.Client()

decodificador = 'etb'
channels = {
    'caracol' : [2,7,6],
    'rcn' : [2,7,7],
    'colombia' : [5,1,0],
    'capital' : [2,5,6]
}

def changeChannel(channel):
    data = control.statusPorts()

    if (channel == 'imbanaco'):
        if data['statusWC'] == 1:
            print(f'la emision esta en canal institucional, nada que hacer')
        else:
            control.alternateChannel()
            print(f'se cambio la emision a institucional')
    else:
        if data['statusWC'] == 0:
            print(f'la emision esta en COMERCIAL, nada que hacer')
            try:
                for tecla in channels[f'{channel}']:
                    print (tecla)
                    clientIR.send_once(decodificador, tecla)
                    time.sleep(1.5)
                time.sleep(3.5)
            except:
                print(f'el canal no esta en la lista de canales COMERCIALES')
        else:
            try:
                for tecla in channels[f'{channel}']:
                    print (tecla)
                    clientIR.send_once(decodificador, tecla)
                    time.sleep(5)
                time.sleep(3.5)
            except:
                print(f'el canal no esta en la lista de canales COMERCIALES')

            control.alternateChannel()
            print(f'se cambio la emision a COMERCIAL')

#changeChannel('capital')
