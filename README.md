# service-iot
iniciativa iot
ref: https://github.com/FIWARE/tutorials.IoT-over-MQTT/blob/master/docker-compose.yml

# Troca de senha
```bash
docker exec -it mosquitto sh
mosquitto_passwd -c /mosquitto/config/pwfile <newsuser>
```

# Cliente teste 

## Instalar programas 
```bash
sudo apt install mosquitto-clients
```

## Teste
ref: http://www.steves-internet-guide.com/mosquitto_pub-sub-clients/


### subcribe
```bash
mosquitto_sub -u locutus -P Zaq12wsX -h 127.0.0.1 -t local/#
```

### publisher
```bash
mosquitto_pub -u locutus -P Zaq12wsX -h 127.0.0.1 -m "teste 123" -t local/t1 -d
```

