# importing vlc module
import vlc
  
# importing time module
import time
  

  
# creating vlc media player object
media_player = vlc.MediaPlayer()
  
# media object
media = vlc.Media("/home/pi/Downloads/media/DIYM/AtmosFX-Story-Sample-DIYMachines.mp4")
  
# setting media to the media player
media_player.set_media(media)
  
# setting video scale
media_player.video_set_scale(0.6)
  
# setting media player role
media_player.set_role(2)
  
  
# setting volume
media_player.audio_set_volume(80)
  
# start playing video
media_player.play()
  
# wait so the video can be played for 5 seconds
# irrespective for length of video
time.sleep(5)