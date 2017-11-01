from socket import *

serverName = '192.168.1.68'
serverPort = 12001
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = raw_input('input lowercase sentence:')
clientSocket.send(sentence.encode())
modifiedSentence, _ = clientSocket.recvfrom(2048)
print('From server: ', modifiedSentence.decode())
clientSocket.close()
