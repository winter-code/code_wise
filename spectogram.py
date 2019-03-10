from scipy.io import wavfile
import matplotlib.pyplot as plt

print("take file ?")
filename= input("Enter file name: ")
floc= "./"+filename+".wav"
fs, data= wavfile.read(floc)

print(fs)

print(data)

plt.plot(data)
plt.show()
