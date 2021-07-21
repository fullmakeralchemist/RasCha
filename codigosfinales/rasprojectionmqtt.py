import vlc
import serial
import paho.mqtt.client as mqtt
import time
ser = serial.Serial('/dev/ttyACM0', 9600)

def ConectarMQTT(client, userdata, flags, rc):
    print("Conencando al Servidor - " + str(rc))


def MensajeMQTT(client, userdata, msg):
    print(f"Mensaje secreto: {msg.topic} - {str(msg.payload)}")


def EnviandoMQTT(client, obj, mid):
    print("Mensaje: " + str(mid))



def LogMQTT(client, obj, level, string):
    print(f"Log: {string}")


while True:
    response = ser.read()
    
    
    MiMQTT = mqtt.Client()
    MiMQTT.on_connect = ConectarMQTT
    MiMQTT.on_publish = EnviandoMQTT
    MiMQTT.on_message = MensajeMQTT
    MiMQTT.on_log = LogMQTT

    MiMQTT.connect("192.168.78.4", 1883)
    
    print(response)
    if (response==b'1'):
        print("playvideo1") #first condition I need
        player= vlc.MediaPlayer('/home/pi/Desktop/media/model4/ink4.mp4')
        player.play()
        player.set_fullscreen(True)
        MiMQTT.publish("room/lamp", "on")
        time.sleep(2)
        MiMQTT.publish("room/lamp", "off")
    if(response==b'2'):
        print("playvideo2") #second condition that I need
        player= vlc.MediaPlayer('/home/pi/Desktop/media/Model1/magic.mp4')
        player.play()
        player.set_fullscreen(True)
        MiMQTT.publish("room/lamp", "on2")
        time.sleep(2)
        MiMQTT.publish("room/lamp", "off")
    if(response==b'3'):
        print("playvideo3") #third condition that I need
        player= vlc.MediaPlayer('/home/pi/Desktop/media/model4/ink1.mp4')
        player.play()
        player.set_fullscreen(True)
        MiMQTT.publish("room/lamp", "on3")
        time.sleep(2)
        MiMQTT.publish("room/lamp", "off")