import lirc,time

clientIR = lirc.Client()
#
# # Go to channel "33"

def onOff():
    clientIR.send_once("kronos", "CH+", repeat_count=1)

def changeChannel(control, tecla1, tecla2):
    clientIR.send_once(control, tecla1, repeat_count=1)
    time.sleep(1)
    clientIR.send_once(control, tecla2, repeat_count=1)
    time.sleep(1)
    # clientIR.send_once(control, tecla, repeat_count=1)
    # time.sleep(1)





def caracol():
    clientIR.send_once("kalley", "ONE" , repeat_count=1)
    time.sleep(1)
    clientIR.send_once("kalley", "SEVEN" , repeat_count=1)
    time.sleep(1)
    # clientIR.send_once("kalley", "four" , repeat_count=1)
    # time.sleep(0.2)

def channelmore():
    clientIR.send_once("kalley", "CH+" , repeat_count=1)
    # time.sleep(1)
    # clientIR.send_once("kalley", "SEVEN" , repeat_count=1)
    # time.sleep(1)
    # clientIR.send_once("kalley", "four" , repeat_count=1)
    # time.sleep(0.2)
