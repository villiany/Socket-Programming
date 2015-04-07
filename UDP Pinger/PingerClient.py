from socket import *
from datetime import datetime

serverName = '127.0.0.1'
clientSocket = socket(AF_INET, SOCK_DGRAM)
serverPort = 12000
clientSocket.settimeout(1)

for i in range(1,11):
    sequence_number=i
    print sequence_number
    ptime = datetime.now()
    ptimestring = ptime.strftime("%H:%M:%S.%f")
    message = 'Ping ' + str(sequence_number) + ' ' + ptimestring
    clientSocket.sendto(message,(serverName,serverPort))
    try:
        modifiedmessage, addr = clientSocket.recvfrom(2048)
        rtt = datetime.now() - ptime
        print "Server Response: " + modifiedmessage
        print "RTT: ",str(rtt.seconds)+"."+str(rtt.microseconds), "seconds \n"
    except timeout:
        print 'Request timed out \n'

if sequence_number == 10:
        clientSocket.close()
