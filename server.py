# Se importa el módulo socket
import socket
from datetime import datetime

# Función para obtener la fecha y hora actual
def get_date():
    return datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

# Variables con la direccion ip y puero de destino de los datagramas
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
BUFFER_SIZE = 1024

# Se inicializa el socket
# el primer argumento se refiere a la familia de direcciones al que pertenece
# el socket, y el segundo al tipo de socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Se asigna la dirección IP y el puerto al que el socket va a escuchar
sock.bind((UDP_IP, UDP_PORT))

print("[{}] Servidor UDP inicializado ...".format(get_date()))

while True:
    # Se especifica al socket que recibira mensajes con la función rcvfrom()
    # el argumento buffer especifica el tamaño de la memoria donde se debe
    # almacenar el mensaje
    data, addr = sock.recvfrom(BUFFER_SIZE)

    # Se convierte el contenido del mensaje de bytes a datos
    # para que puedan ser mostrados de la misma forma en que el usuario los capturo
    print("[{}] {}".format(get_date(), data.decode()))