import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 1235))
serversocket.listen(1) 

buf = []

while True:
    connection, address = serversocket.accept()
    # buf.append(connection.recv(64))
    while True:
        print("{}".format(connection.recv(16)))
        # print(connection.recv(16))
    # if len(buf) > 0:
    #     print (buf)
    #     break