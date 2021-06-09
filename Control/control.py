#!/usr/bin/python3
import time
import RPi.GPIO as GPIO

#Configuracion inicial de los puertos
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
mode = GPIO.getmode()

#Definicion de Puertos
statusWC = 0
lecturaestadoWC = 31
cambiarCanal = 15

GPIO.setup(cambiarCanal, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(lecturaestadoWC, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Simula el boton en el HDMI
def alternateChannel():
    GPIO.output(cambiarCanal, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(cambiarCanal, GPIO.LOW)
    time.sleep(1.5)


def statusPorts():
    #Lectura del switch HDMI
    if (GPIO.input(lecturaestadoWC) == GPIO.HIGH):
        data = {
           'currentStreaming': 'Canal Institucional',
           'statusWC' : 1
           }
    else:
        data = {
           'currentStreaming': 'Canal Comercial',
            'statusWC' : 0
           }
    return data

statusStreaming = statusPorts()
print(statusStreaming)
