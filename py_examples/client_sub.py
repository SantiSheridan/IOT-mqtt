import paho.mqtt.client as mqtt

# Definir las funciones de callback
def on_connect(client, userdata, flags, rc):
    print("Cliente Sub conectado con código de resultado "+str(rc))
    # Suscribirse a un tópico
    client.subscribe("test/topic")

def on_message(client, userdata, msg):
    print("Mensaje recibido: "+str(msg.payload.decode()))

# Crear una instancia del cliente
client = mqtt.Client()
client.username_pw_set("patagonia", "122333")

# Asignar las funciones de callback
client.on_connect = on_connect
client.on_message = on_message

# Conectarse al broker
client.connect("192.168.0.187", 1883, 60)

# Mantener el cliente en ejecución
client.loop_forever()