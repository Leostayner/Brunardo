
import socket
import sys

class transmissao():
    
    def __init__(self, mensagem):
        
        print(mensagem)

        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = ('localhost', 1240)
        
        print (sys.stderr, 'connecting to %s port %s' % server_address)
        sock.connect(server_address) 

        try:
            
            # Send data
            message = mensagem
            bmessage = str.encode(message)
            print (sys.stderr, 'sending "%s"' % bmessage)
            sock.sendall(bmessage)
            

        finally:
            print (sys.stderr, 'closing socket')
            sock.close()