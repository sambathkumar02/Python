#!usr/bin/python
'''
This is the client for message sending application between two hosts
using TCP/IP socket
'''

import socket
import threading
from threading import *

#socket for client
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)



# function of sending messages running on main thread
def sending():
    print('----------------------------------MESSAGE SENDING PORTAL-----------------------------------')
    while True:
        message = input('>')                                            #prompt for user message entry
        client.sendall(bytearray(message, 'utf-8'))                     #send message to server
        print('you:', message)


#Thread for receiving message from server
class reciever(Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):

        while True:
            message = None                                              #checking  variable for recieved message
            isprint=False                                               #checking variable for message is printed or n
            while True:
                while message == None:
                        message = client.recv(4096).decode()                #recieving message from server
                if isprint==False:
                        print('\noponent:', message)
                        isprint=True
                message=None
                isprint=False




#object for Reciever Thread
recieving=reciever()


#condition varialbles
connection=False                                            #checking for connection established or not
check='notok'                                               #Acknowlwdgement from the server
i=0
check_bool=False


server_ip=input("Enter ip address of server(running on same system set 'localhost'):")      #Getting ip address of server


#checking for the connection
while (connection==False & check_bool==False):
    try:
        client.connect((server_ip,2222))
        print('connection established with the server..')
        connection=True
        while check_bool!=True:
            check=client.recv(1024).decode()
            if check=='ok':
                check_bool=True
    except Exception:
        print('cant reach server at the moment.....')
        print('try to reach server.....')

print('connected with opponent!')

#Starting the operations
recieving.start()                                            #starting reciever Thread
sending()                                                    #calling sending function

#closing connection
client.close()






