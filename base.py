import vlc
import serial
ser = serial.Serial('/dev/ttyACM0', 9600)

while True :
    try:
        response = ser.read()
        print(response)
        if (response==b'1'):
            print("playvideo1") #first condition I need
        elif(response==b'2'):
            print("playvideo2") #second condition that I need
        elif(response==b'3'):
            print("playvideo3") #third condition that I need
    except:
        pass