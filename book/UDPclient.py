from socket import *

serverName = 'hostname'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = raw_input('input lowercase sentence:')
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, severAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()