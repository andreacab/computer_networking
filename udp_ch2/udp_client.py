from socket import *

HOST = 'hostname'
PORT = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = raw_input('Input lowercase sentence:')
clientSocket.sendto(message.encode(), (HOST, PORT))
modifiedMessage, serverAddress = clientSocket.recvFrom(2048)
print(modifiedMessage.decode())
clientSocket.close()