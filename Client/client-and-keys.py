#!/usr/bin/env python3
#import everything needed

import socket
from inputs import get_key

HOST = '192.168.1.58'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data))


#define methods for movement
def forward():
    print ("forwards running  motor ")
    s.sendall(b'KEY_UP')

def backward():
    print ("backwards running motor")
    s.sendall(b'KEY_DOWN')

def left():
    print ("left running  motor ")
    s.sendall(b'KEY_LEFT')

def right():
    print ("right running motor")
    s.sendall(b'KEY_RIGHT')

def stop():
    print("stopping...")
    s.sendall(b'KEY_1')

#create go until said to stop loop
go = True

while (go == True):
    #get the key typed
    events = get_key()
    if events:
        code = ""
        key = ""
        for event in events:
              #print(event.ev_type, event.code, event.state)
            #TEST print(event.code)
            code = event.code
            if (code.find("KEY") == 0):
                key = event.code
            print(key)

        #move or stop
        if (key == "KEY_1"):
            stop()
        elif (key == "KEY_2"):
            go = false
            s.sendall(b'KEY_2')
        elif (key == "KEY_UP"):
           forward()
        elif (key == "KEY_DOWN"):
            backward()
        elif (key == "KEY_RIGHT"):
            right()
        elif (key == "KEY_LEFT"):
            left()
        else:
            print("key not in code. You typed..." + key)




