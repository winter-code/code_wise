
import pyaudio

CHUNK = 1500
WIDTH = 5
CHANNELS = 2
RATE = 55000
RECORD_SECONDS = 10

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)

print("* recording")

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)  #read audio stream
    stream.write(data, CHUNK)  #play back audio stream
    print(' ****************************')
    #print(data)
print("fcgvfsx fuck off")
stream.stop_stream()
stream.close()
p.terminate()
