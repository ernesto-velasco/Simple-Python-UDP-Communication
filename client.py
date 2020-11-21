import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

print("Cliente UDP inicializado ...")
while True:
    print("Escribe el mensaje que quieres enviar. (Mensaje vacio para salir)")
    MESSAGE = input()
    if not MESSAGE: break
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))