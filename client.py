# Se importa el módulo socket
import socket

def main():
    # Variables con la direccion ip y puero de destino de los datagramas
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005

    print("Cliente UDP inicializado ...")

    while True:
        # Creación del mensaje
        print("Escribe el mensaje que quieres enviar. (Mensaje vacio para salir)")
        MESSAGE = input()

        if not MESSAGE: break

        # Se inicializa el socket
        # el primer argumento se refiere a la familia de direcciones al que pertenece
        # el socket, y el segundo al tipo de socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # Se envía  el mensaje
        # el primer argumento es el mensaje que se convertido a bytes
        # el segundo argumento es la dirección
        sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))

if __name__ == "__main__":
    main()