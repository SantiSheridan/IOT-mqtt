import paho.mqtt.client as mqtt
import time
# Definir las funciones de callback
def on_connect(client, userdata, flags, rc):
    print("Cliente 1 conectado con código de resultado "+str(rc))
    # Publicar un mensaje en el tópico
    client.publish("test/topic", "Mensaje desde Cliente Pub")

# Crear una instancia del cliente
client = mqtt.Client()
client.username_pw_set("patagonia", "122333")

# Asignar las funciones de callback
client.on_connect = on_connect

# Conectarse al broker
client.connect("192.168.0.187", 1883, 60)

# Mantener el cliente en ejecución
client.loop_start()
count = 0
while True:
    client.publish("test/topic", "Mensaje desde Pub: {}".format(count))
    count+=1
    time.sleep(5)
    pass
 