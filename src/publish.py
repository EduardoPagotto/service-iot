#!/usr/bin/env python3
'''
Created on 20200105
Update on 20200105
@author: Eduardo Pagotto
 '''

import paho.mqtt.publish as publish

if __name__ == '__main__':

    # Publica
    publish.single("topico/teste", "Oi, aqui é um teste", hostname="127.0.0.1", auth={'username':'locutus', 'password':'Zaq12wsX'})

