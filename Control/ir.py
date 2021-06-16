import lirc,time
from Control import control


clientIR = lirc.Client()

decodificador = 'kronos'
channels = {
    'caracol' : [0,1],
    'rcn' : [0,5],
    'colombia' : [0,6],
    'capital' : [1,1]
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
                    clientIR.send_once(decodificador, tecla, repeat_count=1)
                    time.sleep(1)
                time.sleep(3.5)
            except:
                print(f'el canal no esta en la lista de canales COMERCIALES')
        else:
            try:
                for tecla in channels[f'{channel}']:
                    print (tecla)
                    clientIR.send_once(decodificador, tecla, repeat_count=1)
                    time.sleep(1)
                time.sleep(3.5)
            except:
                print(f'el canal no esta en la lista de canales COMERCIALES')

            control.alternateChannel()
            print(f'se cambio la emision a COMERCIAL')

# changeChannel('capital')
