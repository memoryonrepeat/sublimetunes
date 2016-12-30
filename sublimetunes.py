# Reference: https://stackoverflow.com/a/25899180/1442280
# Use attached vlc file since it's not on pip
import vlc
p = vlc.MediaPlayer("http://www.stephaniequinn.com/Music/Pachelbel%20-%20Canon%20in%20D%20Major.mp3")
p.play()