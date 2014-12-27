__author__ = 'sam'
"""
Sample code to learn socket programming in python through socket module use.
Here we are opening a port and receving on it.
Clients can connect to the port to have communication.
"""
import socket               # Import socket module
import os
import subprocess
import sys

s = socket.socket()         # Create a socket object
host = '' 

port = int(sys.argv[1])
s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for mac 5client connection.
print "SERVER STARTED and listening on " 

while True:
    connection, addr = s.accept()     # Establish connection with client.
    #listening started
    msg="STARTED connection" 
    connection.send(msg)
    try:
        print 'connection from', addr
            # Receive the data in small chunks and retransmit it
        while True:
            remoteCommand = connection.recv(100)
            print 'SERVER : received command "%s"' % remoteCommand


            p = subprocess.Popen(remoteCommand ,stdout=subprocess.PIPE, shell=True)
            out, err = p.communicate()
            print out
            connection.sendall(str(out))
            print "============="
            print "RESULT SENT TO CLIENT " + str(addr)
            print "============="
            break
            """
            if remoteCommand:
                print 'SERVER: sending remoteCommand back to the client'
                connection.sendall(remoteCommand)
            else:
                print 'SERVER: no more remoteCommand from', addr
                break
            """
    finally:
            # Clean up the connection
            connection.close()

