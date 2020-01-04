# Importa o publish do paho-mqtt
import paho.mqtt.publish as publish
# Publica

publish.single("topico/teste", "Oi, aqui é um teste", hostname="127.0.0.1", auth={'username':'locutus', 'password':'Zaq12wsX'})

