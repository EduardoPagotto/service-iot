#!/usr/bin/env python3
'''
Created on 20200105
Update on 20200105
@author: Eduardo Pagotto
 '''

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
'''[The callback for when the client receives a CONNACK response from the server]
Arguments:
    client {[type]} -- [description]
    userdata {[type]} -- [description]
    flags {[type]} -- [description]
    rc {[type]} -- [description]
'''
    # O subscribe fica no on_connect pois, caso perca a conexão ele a renova
    # Lembrando que quando usado o #, você está falando que tudo que chegar após a barra do topico, será recebido
    client.subscribe("topico/#")

def on_message(client, userdata, msg):
"""[Callback responável por receber uma mensagem publicada no tópico acima]
Arguments:
    client {[type]} -- [description]
    userdata {[type]} -- [description]
    msg {[type]} -- [description]
"""
    print(msg.topic+" -  "+str(msg.payload))

if __name__ == '__main__':

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    # Seta um usuário e senha para o Broker, se não tem, não use esta linha
    client.username_pw_set("locutus", password="Zaq12wsX")

    # Conecta no MQTT Broker, no meu caso, o Mosquitto
    client.connect("127.0.0.1", 1883, 60)

    # Inicia o loop
    client.loop_forever()