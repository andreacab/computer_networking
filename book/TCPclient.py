from socket import *

serverName = '108.180.181.245'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = raw_input('input lowercase sentence:')
clientSocket.send(message.encode())
modifiedSentence = clientSocket.recvfrom(2048)
print('From server: ', modifiedSentence.decode())
clientSocket.close()
