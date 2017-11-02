# curl ipinfo.io/ip to find your ip
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print('The server is ready to receive')
while True:
	connectionSocket, addr = serverSocket.accept()
	message = connectionSocket.recv(1024)
	print("From client: ", addr)
	print("With message: ", message.decode())
	connectionSocket.send('received!'.encode())
	connectionSocket.close()
    
    
    
    
