#import socket module
from socket import *
import sys # In order to terminate the program
import threading
import logging


# Configure logger
logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

def worker(connSocket, address):
    try:
        message = connSocket.recv(2048)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()

        logging.debug('Read file successfully')

        #Send one HTTP header line into socket
        connSocket.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n".encode())

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connSocket.send(outputdata[i].encode())
        connSocket.send("\r\n".encode())
    except IOError:
        logging.debug('Could not read file')
        #Send response message for file not found
        connSocket.send("HTTP/1.1 404 NOT FOUND\r\n\r\n")

    #Close client socket
    connSocket.close()

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
HOST = '' # INADDR_ANY
PORT = 6789
serverSocket.bind((HOST, PORT))
serverSocket.listen(5)

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, _addr = serverSocket.accept()
    logging.debug('accepted connection on: ' + str(_addr))
    t = threading.Thread(target=worker, args=(connectionSocket, _addr))
    t.start()

serverSocket.close()
sys.exit() #Terminate the program after sending the corresponding data


