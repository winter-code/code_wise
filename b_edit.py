from scipy.io import wavfile
import matplotlib.pyplot as plt

path=input("Enter directory : ")

l=[]

for i in range(3):
	Input_file= "./"+ path+"/file"+str(i)+".wav"

	fs, data= wavfile.read(Input_file)
	l.append(data)
	print(fs)

	print(data)
	



	

	plt.subplot(2, 1, 1)

	plt.plot(data)	
	plt.title('DIfference in spectrograms')
	plt.ylabel('Frequencies together')

plt.subplot(2, 1, 2)
plt.plot(l[0]-l[1])
plt.xlabel('time')
plt.ylabel('Seperated')

plt.show()


