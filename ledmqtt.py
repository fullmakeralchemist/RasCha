import paho.mqtt.client as mqtt
import time


def ConectarMQTT(client, userdata, flags, rc):
    print("Conencando al Servidor - " + str(rc))


def MensajeMQTT(client, userdata, msg):
    print(f"Mensaje secreto: {msg.topic} - {str(msg.payload)}")


def EnviandoMQTT(client, obj, mid):
    print("Mensaje: " + str(mid))



def LogMQTT(client, obj, level, string):
    print(f"Log: {string}")


MiMQTT = mqtt.Client()
MiMQTT.on_connect = ConectarMQTT
MiMQTT.on_publish = EnviandoMQTT
MiMQTT.on_message = MensajeMQTT
MiMQTT.on_log = LogMQTT

MiMQTT.connect("192.168.29.4", 1883)

MiMQTT.publish("dance/lights", "off")
time.sleep(9)
MiMQTT.publish("dance/lights", "on")
time.sleep(9)
MiMQTT.publish("dance/lights", "off")

MiMQTT.loop_forever()