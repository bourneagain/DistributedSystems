__author__ = 'sam'
"""
This is the client which starts connecting to the servers and then issues commands
"""
import socket
import sys
import os

# Create a TCP/IP socket

filename,server1,port1,server2,port2,command=sys.argv
server_addressList = [ (server1,int(port1) ),(server2,int(port2) )]
print server_addressList

for sa in server_addressList:
    print 'connecting to %s port %s' % sa
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(sa)
    data = sock.recv(1000)
    print "RECEIVED FROM SERVER " + data

    try:
    # Send command
        print 'CLIENT: sending "%s"' % command
        #######################
        sock.sendall(command)
        #######################
        data = sock.recv(1000)
		print "========================="
		print " OP: "  + data
		print "========================"

    finally:
        print "DONE WITH RECEIVING INFO FROM " + str(sa)
        print 'CLIENT: closing socket'
        sock.close()
