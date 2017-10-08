from socket import *

HOST = '192.168.1.64'
PORT = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
while True
    message = raw_input('Input lowercase sentence:')
    break if message == 'q' || message == 'quit' || message == 'exit'
    print('sending message...')
    clientSocket.sendto(message.encode(), (HOST, PORT))
    response, serverAddress = clientSocket.recvfrom(2048)
    print(response, ", from ", serverAddress, sep="")

clientSocket.close()