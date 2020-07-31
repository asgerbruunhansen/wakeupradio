import alsaaudio
import time
m = alsaaudio.Mixer()

newVol = 0
m.setvolume(newVol)

vol = m.getvolume()
vol = int(vol[0])

while vol < 99:
    vol = m.getvolume()
    vol = int(vol[0])
    newVol = vol + 1
    m.setvolume(newVol)
    time.sleep(0.03)
    
print("fade-up complete")