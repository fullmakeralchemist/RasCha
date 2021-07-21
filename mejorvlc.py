import vlc
import time

instance = vlc.Instance()
player = instance.media_player_new()
media = instance.media_new('/home/pi/Downloads/media/DIYM/AtmosFX-Story-Sample-DIYMachines.mp4')
player.set_media(media)
player.play()
player.set_fullscreen(True)


while player.get_state() != vlc.State.Ended:
    time.sleep(1)  # Solo para evitar un uso innecesario de CPU
    playerstate = str(player.get_state())
    # printing the duration of the video
    print("State : " + str(playerstate))
    if (playerstate=="State.Ended"):
        player.stop()
