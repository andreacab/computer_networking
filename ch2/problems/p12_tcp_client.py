from socket import *

serverName = 'servername'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    message = raw_input('Input lowercase sentence:')
    
    if (message == 'q') or (message == 'quit') or (message == 'exit'):
        break
        
    print('sending message...')
    clientSocket.send(message.encode())
    
    receive = clientSocket.recv(1024)
    print('From server: ', receive.decode())
    
clientSocket.close()
