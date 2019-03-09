from scipy.io import wavfile
import matplotlib.pyplot as plt

path=input("Enter directory : ")
for i in range(2):
	Input_file= path+"/file"+str(i)+".wav"
	fs, data= wavfile.read(Input_file)

	print(fs)

	print(data)

	plt.plot(data)
	plt.show()
