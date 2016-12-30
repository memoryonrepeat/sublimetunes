# Reference: https://stackoverflow.com/a/25899180/1442280
# Use attached vlc file since it's not on pip

# How noisli works:
# First a .m3u8 file is fetched. It's simple a textfile that works like a playlist
# that comprises of multiple .ts file (equivalent to MPEG2, playable by vlc both offline and online)
# When user selects a theme, noisli will download and play the corresponding .ts file 

sample_mp3 = "http://www.stephaniequinn.com/Music/Pachelbel%20-%20Canon%20in%20D%20Major.mp3"
sample_ts = "https://storage.googleapis.com/noisli/hls/forest/hls_160_00003.ts"
sample_m3u8 = "https://storage.googleapis.com/noisli/hls/forest/forest.m3u8"

import vlc
p = vlc.MediaPlayer(sample_ts)
p.play()