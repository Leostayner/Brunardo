# Camada Física da Computação
# Exemplo socket server 
## https://pymotw.com/2/socket/tcp.html

import socket
import sys
import time

class recepcao(object):
    def __init__(self):
        PORTA = 1233

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
            self.connection, client_address = sock.accept()
            if(self.connection.accept):
                break

    def get(self):
        
        try:
        # Receive the data in small chunks and retransmit it
            temp = b''
            while True:
                data = self.connection.recv(2)
                temp+=data
            
                # data = byToString(data)
                try:
                    a = temp.decode()
                    temp = b''

                    print("essa é a letra: {}".format(a))
                    return a

                except UnicodeDecodeError:
                    pass

                if(len(data) <= 0):
                    break

                time.sleep(0.5) 
        except:
            pass       

        # finally:
        # #     # Clean up the connection
        #     self.connection.close()

if __name__ == "__main__":
    main()
