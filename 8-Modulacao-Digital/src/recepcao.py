# Camada Física da Computação
# Exemplo socket server 
## https://pymotw.com/2/socket/tcp.html

import socket
import sys

def main():
    PORTA = 1235

    print("Inicializando socket TCP/IP")
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = ('localhost', PORTA)
    print("PORTA {}".format(PORTA))
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    while True:
        # Wait for a connection
        print("waiting for a connection")
        connection, client_address = sock.accept()

        try:
            print(" connection from {}".format(client_address))

            # Receive the data in small chunks and retransmit it
            temp = b''
            while True:
                data = connection.recv(2)
                temp+=data

                # data = byToString(data)
                try:
                    a = temp.decode()
                    temp = b''

                    print("{}".format(a))
                

                except UnicodeDecodeError:
                    pass

                if(len(data) <= 0):
                    break
                

        finally:
            # Clean up the connection
            connection.close()


## Convet para String.
def byToString(value):
    a = value.decode()


    # print(type(a))
    # b = value.decode('utf-8', 'ignore')

    # b = unicode(a, errors='replace')
    return value


if __name__ == "__main__":
    main()
