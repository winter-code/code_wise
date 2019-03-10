from pydub import AudioSegment
audio=AudioSegment.from_mp3("./hello.mp3")
audio.export("./hello.wav", format="wav")