# Reference: https://stackoverflow.com/a/25899180/1442280
# Use attached vlc file since it's not on pip
import vlc
p = vlc.MediaPlayer("westcoast.mp3")
p.play()