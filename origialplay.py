import vlc
import serial
ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
    
    response = ser.read()
    print(response)
    if (response==b'1'):
        print("playvideo1") #first condition I need
    if(response==b'2'):
        print("playvideo2") #second condition that I need
    if(response==b'3'):
        print("playvideo3") #third condition that I need
        player= vlc.MediaPlayer('/home/pi/Downloads/media/DIYM/AtmosFX-Story-Sample-DIYMachines.mp4')
        player.play()
        player.set_fullscreen(True)