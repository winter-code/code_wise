from scipy.io import wavfile
import matplotlib.pyplot as plt

fs, data= wavfile.read('./a1file.wav')

print(fs)

print(data)

plt.plot(data)
plt.show()
