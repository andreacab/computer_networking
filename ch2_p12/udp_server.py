from socket import *

serverPort = 12000
serverSocket = socket.socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready to receive')
while True:
    message, clientAddress = serverSocket.recvFrom(2048)
    print("From client: ", clientAddress)
    print("With message: ", message.decode())
    serverSocket.sendTo('received!', clientAddress)