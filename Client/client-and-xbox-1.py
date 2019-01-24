#!/usr/bin/env python3
#import everything needed

import socket
from inputs import get_gamepad

HOST = '192.168.1.58'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data))


#define methods for movement
def mapit(joystick):
    num = abs(joystick)

    #defining directions and which controller
    if(code.find("ABS_X") == 0):
        direction = "X"
        side = "L"
    elif(code.find("ABS_Y") == 0):
        direction = "Y"
        side = "L"
    elif(code.find("ABS_RX") == 0):
        direction = "X"
        side = "R"
    else:
        direction = "Y"
        side = "R"

    #mapping pwm 
    if(num>30000):
        pwm = "100"
    elif(num<4000 and num>-4000):
        pwm = "0"
    elif(num<-30000):
        pwm = "-100"
    else:
        pwm=str(round(num/300)

    #sending
    send = "PWM," + pwm + "," + direction + "," + side
    s.sendall(send.encode())
        

def buttons(event_code, event_state):
    button = event_code
    state = event_state

    #define letter
    if(button == "BTN_TL"):
        letter = "TL"
    elif(button =="BTN_TR"):
        letter = "TR"
    elif(button =="BTN_NORTH"):
        letter = "Y"
    elif(button =="BTN_SOUTH"):
        letter = "A"
    elif(button =="BTN_EAST"):
        letter = "B"
    elif(button =="BTN_WEST"):
        letter = "X"

    #turn off
    if(state == "1"):
        state = "on"
    else:
        state = "off"

    #send
    s.sendall(encode("BTN," + letter + state))

def hato(event_code, event_state):
    name = event_code.split("_")
    movement = str(event_state)

    #assign directions
    if(name[2] == "HATOY"):
        arrow = "Y"
    else:
        arrow = "X"

    #send
    s.sendall(encode(arrow + "'" + movement))
        

#create go until said to stop loop
go = True

while (go == True):
    #get the key typed
    events = get_gamepad()
    code = ""
    key = ""
    for event in events:
        #print(event.ev_type, event.code, event.state)
        #TEST print(event.code)
        code = event.code
        state2 = event.state
        begin = code.split("_")
        if (begin[0] == "BTN"):
            print("button")
            buttons(event.code, event.state)
        elif (begin[1] == "HATOX" or begin[1] == "HATOY"):
            hato(event.code, event.state)
            print("arrows")
        else:
            mapit(event.code, event.state)
            print("joystick")
        




