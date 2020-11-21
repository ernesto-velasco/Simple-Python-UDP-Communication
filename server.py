import socket
from datetime import datetime

def get_date():
    return datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print("[{}] Servidor UDP inicializado ...".format(get_date()))

while True:
    data, addr = sock.recvfrom(BUFFER_SIZE)
    print("[{}] {}".format(get_date(), data.decode()))