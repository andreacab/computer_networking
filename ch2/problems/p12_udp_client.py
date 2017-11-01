from socket import *

HOST = '75.155.164.149'
PORT = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
while True:
    message = raw_input('Input lowercase sentence:')
    if (message == 'q') or (message == 'quit') or (message == 'exit'):
        break
    print('sending message...')
    clientSocket.sendto(message.encode(), (HOST, PORT))
    response, serverAddress = clientSocket.recvfrom(2048)
    print(response + ", from " + str(serverAddress))

clientSocket.close()