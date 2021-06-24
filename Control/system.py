import psutil, pprint, json

def statusAlternadora():
    # pprint.pprint(psutil.net_if_addrs())
    load = psutil.cpu_percent(interval=None)
    sensors = psutil.sensors_temperatures()['cpu_thermal'][0]
    networkAddress = psutil.net_if_addrs()['eth0'][0]
    networkMac = psutil.net_if_addrs()['eth0'][2]
    
    status = {
        "status": 'connected',
        "currentLoad": f'{load}',
        "main": f'{sensors.current}',
        "ip4": f'{networkAddress.address}',
        "MAC": f'{networkMac.address}'
    }
    return status
    
