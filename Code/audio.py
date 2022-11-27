from __modules__ import *
import mainFunctions as fs

Audio = AudioManager(20, (6, 0))

suoni = fs.fill(Sound_path)
musica = fs.fill(Music_path)

for fx in suoni:
   char = "-"
   
   if char not in fx:
      char = ".wav"
   
   Audio.AddSound(fx.split(char)[0], Sound_path + fx, 2)
   
for fx in musica:
   char = "-"
   
   if char not in fx:
      char = ".wav"
      
   Audio.AddMusic(fx.split(char)[0], Music_path + fx, 1.5)
   
print(Audio.Volume)