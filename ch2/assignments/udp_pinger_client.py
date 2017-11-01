from socket import *
from datetime import datetime

clientSocket = socket(AF_INET, SOCK_DGRAM)
SERVER = '192.168.1.67' # localhost
PORT = 12000

clientSocket.settimeout(1.0)
for i in range(1, 11):
    clientSocket.connect((SERVER, PORT))
    sentTime = datetime.now()
    clientSocket.send(" ".join(["Ping", str(i), sentTime.strftime('%Y-%m-%d_%H:%M:%S')]).encode())

    try:
        message = clientSocket.recv(1024).decode()
        recvTime = datetime.now()
        if message is not None:
            print message
        timeDifference = sentTime - recvTime
        print "RTT is " + str(timeDifference.total_seconds())
    except timeout:
        print "Request timed out"



