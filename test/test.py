import android
from AidLux import Aashmem
import wave
import time
channels = 1
filename = "output.wav"
path="/tmp/mmkv/tmp_audio"
fs = 44100 
switch=True
droid=android.Android()
result=droid.audioSampling(switch,fs,"MIC","MONO","16BIT",True)
time.sleep(1)
print(result)
frames = [] 
l=0
time1=time.time()
if switch:
    ashmem=Aashmem(path)
    while True:
        l = int.from_bytes(ashmem.get_bytes(4, 0), byteorder='little')
        if l==0:
            continue
        print(l)
        data = ashmem.get_bytes(l, 4)
        frames.append(data)
        l=0
        ashmem.set_bytes(l.to_bytes(4, byteorder='little', signed=True), 4, 0)
        print(len(data))
        time2=time.time()
        if time2-time1>5:
            break
print(len(frames))
switch=False
result=droid.audioSampling(switch)
print('录音结束')
wf = wave.open(filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(2)
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()